import cv2
import time


class QRDetector:

    def __init__(self):

        self.detector = cv2.QRCodeDetector()

    def decode(self, frame):

        start = time.perf_counter()

        data, points, _ = self.detector.detectAndDecode(frame)

        elapsed = (time.perf_counter() - start) * 1000

        return data, points, elapsed