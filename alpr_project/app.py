import cv2
import csv
import os
import numpy as np

from camera.mock_camera import MockCamera
from detector.roboflow_detector import PlateDetector
from ui.dashboard import Dashboard


# ----------------------------------
# Setup
# ----------------------------------

os.makedirs(
    "output",
    exist_ok=True
)

os.makedirs(
    "output/crops",
    exist_ok=True
)

camera = MockCamera(
    "data"
)

detector = PlateDetector()

dashboard = Dashboard()


# ----------------------------------
# CSV
# ----------------------------------

csv_path = "output/results.csv"

csv_file = open(
    csv_path,
    "w",
    newline="",
    encoding="utf-8"
)

writer = csv.writer(
    csv_file
)

writer.writerow(
    [
        "image_name",
        "confidence"
    ]
)

crop_counter = 0


# ----------------------------------
# Main Loop
# ----------------------------------

while True:

    success, image_path = camera.read()

    if not success:
        break

    frame = cv2.imread(
        image_path
    )

    image_name = os.path.basename(
        image_path
    )

    detections = detector.detect(
        image_path
    )

    highest_confidence = None

    for detection in detections:

        x1, y1, x2, y2 = (
            detection["bbox"]
        )

        confidence = (
            detection["confidence"]
        )

        highest_confidence = confidence

        # Draw box
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        # Draw confidence
        cv2.putText(
            frame,
            f"{confidence:.2f}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        # Crop plate
        crop = frame[
            max(0, y1):min(frame.shape[0], y2),
            max(0, x1):min(frame.shape[1], x2)
        ]

        crop_name = (
            f"plate_{crop_counter}.jpg"
        )

        crop_path = os.path.join(
            "output",
            "crops",
            crop_name
        )

        if crop.size > 0:

            cv2.imwrite(
                crop_path,
                crop
            )

        writer.writerow(
            [
                image_name,
                round(confidence, 4)
            ]
        )

        crop_counter += 1

    dashboard.update(
        image_name=image_name,
        confidence=highest_confidence
    )

    frame = cv2.resize(
        frame,
        (900, 700)
    )

    dashboard_panel = (
        dashboard.build_panel()
    )

    combined = np.hstack(
        [
            frame,
            dashboard_panel
        ]
    )

    cv2.imshow(
        "ALPR Roboflow Detector",
        combined
    )

    key = cv2.waitKey(1000)

    if key == ord("q"):
        break


# ----------------------------------
# Cleanup
# ----------------------------------

csv_file.close()

cv2.destroyAllWindows()

print("\nProcessing Complete")
print(
    f"Frames Processed: "
    f"{dashboard.frames_processed}"
)
print(
    f"Detections: "
    f"{dashboard.total_detections}"
)