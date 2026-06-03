import cv2
import csv
import os
import numpy as np

from camera.mock_camera import MockCamera
from detector.qr_detector import QRDetector
from ui.dashboard import Dashboard


DATA_FOLDER = "data"

image_count = len([
    f for f in os.listdir(DATA_FOLDER)
    if f.lower().endswith(
        (".png", ".jpg", ".jpeg")
    )
])

#for real camera, use:
#cap = cv2.VideoCapture(0)
#success, frame = cap.read()


camera = MockCamera(DATA_FOLDER, fps=2)

detector = QRDetector()

dashboard = Dashboard(
    target_unique_qrs=image_count
)

os.makedirs("output", exist_ok=True)

csv_file = open(
    "output/results.csv",
    "w",
    newline="",
    encoding="utf-8"
)

writer = csv.writer(csv_file)

writer.writerow([
    "decoded_qr"
])

saved = set()

while True:

    success, frame = camera.read()

    if not success:
        break

    data, points, elapsed = detector.decode(frame)

    dashboard.update(
        data,
        elapsed
    )

    if data and data not in saved:

        writer.writerow([data])

        saved.add(data)

    if points is not None:

        points = points.astype(int)

        for i in range(len(points[0])):

            p1 = tuple(points[0][i])

            p2 = tuple(
                points[0][
                    (i + 1)
                    % len(points[0])
                ]
            )

            cv2.line(
                frame,
                p1,
                p2,
                (0, 255, 0),
                3
            )

    # Resize camera feed
    frame = cv2.resize(
        frame,
        (800, 600)
    )

    dashboard_panel = dashboard.build_panel()

    combined = np.hstack([
        frame,
        dashboard_panel
    ])

    cv2.imshow(
        "QR Scanner",
        combined
    )

    if dashboard.completed():

        cv2.waitKey(2000)

        print(
            "\nAll unique QR codes detected."
        )

        break

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

csv_file.close()

cv2.destroyAllWindows()