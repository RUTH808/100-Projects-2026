import cv2
import numpy as np


class Dashboard:

    def __init__(self, target_unique_qrs):

        self.frames = 0
        self.qrs_found = 0

        self.decode_times = []

        self.unique_qrs = set()

        self.last_data = ""

        self.target_unique_qrs = target_unique_qrs

    def update(self, data, decode_time):

        self.frames += 1

        self.decode_times.append(decode_time)

        if data:

            self.qrs_found += 1

            self.unique_qrs.add(data)

            self.last_data = data

    def avg_time(self):

        if not self.decode_times:
            return 0

        return round(
            sum(self.decode_times) / len(self.decode_times),
            2
        )

    def completed(self):

        return (
            len(self.unique_qrs)
            >= self.target_unique_qrs
        )

    def build_panel(self):

        panel = np.full(
            (600, 350, 3),
            245,
            dtype=np.uint8
        )

        cv2.putText(
            panel,
            "QR DASHBOARD",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 0, 0),
            2
        )

        stats = [
            f"Frames: {self.frames}",
            f"QR Detections: {self.qrs_found}",
            f"Unique QRs: {len(self.unique_qrs)}",
            f"Target QRs: {self.target_unique_qrs}",
            f"Avg Decode: {self.avg_time()} ms",
        ]

        y = 100

        for text in stats:

            cv2.putText(
                panel,
                text,
                (20, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (40, 40, 40),
                2
            )

            y += 50

        cv2.line(
            panel,
            (20, 320),
            (320, 320),
            (180, 180, 180),
            2
        )

        cv2.putText(
            panel,
            "Last QR:",
            (20, 360),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 0),
            2
        )

        last = self.last_data[:35]

        cv2.putText(
            panel,
            last,
            (20, 410),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (80, 80, 80),
            1
        )

        if self.completed():

            cv2.putText(
                panel,
                "SCAN COMPLETE",
                (20, 540),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 150, 0),
                3
            )

        return panel