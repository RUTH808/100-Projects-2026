import cv2
import numpy as np


class Dashboard:

    def __init__(self):

        self.frames_processed = 0

        self.total_detections = 0

        self.confidences = []

        self.last_confidence = 0

        self.last_image = ""

    def update(
        self,
        image_name,
        confidence=None
    ):

        self.frames_processed += 1

        self.last_image = image_name

        if confidence is not None:

            self.total_detections += 1

            self.last_confidence = confidence

            self.confidences.append(
                confidence
            )

    def average_confidence(self):

        if not self.confidences:
            return 0

        return round(
            sum(self.confidences)
            / len(self.confidences),
            3
        )

    def build_panel(self):

        panel = np.full(
            (700, 400, 3),
            245,
            dtype=np.uint8
        )

        cv2.putText(
            panel,
            "ALPR DASHBOARD",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 0, 0),
            2
        )

        stats = [
            f"Frames Processed: {self.frames_processed}",
            f"Detections: {self.total_detections}",
            f"Avg Confidence: {self.average_confidence()}",
            f"Last Confidence: {round(self.last_confidence,3)}",
            f"Last Image:",
            self.last_image
        ]

        y = 120

        for stat in stats:

            cv2.putText(
                panel,
                stat,
                (20, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.65,
                (40, 40, 40),
                2
            )

            y += 70

        return panel