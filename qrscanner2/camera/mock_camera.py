import cv2
import os
import time


class MockCamera:

    def __init__(self, image_folder, fps=2):

        self.files = [
            os.path.join(image_folder, f)
            for f in os.listdir(image_folder)
            if f.lower().endswith(
                (".png", ".jpg", ".jpeg")
            )
        ]

        self.index = 0
        self.delay = 1.0 / fps

    def read(self):

        if not self.files:
            return False, None

        path = self.files[self.index]

        frame = cv2.imread(path)

        self.index += 1

        if self.index >= len(self.files):
            self.index = 0

        time.sleep(self.delay)

        return True, frame