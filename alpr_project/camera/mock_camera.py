import cv2
import os
import time


class MockCamera:

    def __init__(self, folder, fps=2):

        self.files = sorted([
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if f.lower().endswith(
                (".jpg", ".jpeg", ".png")
            )
        ])

        self.index = 0
        self.delay = 1 / fps

    def read(self):

        if self.index >= len(self.files):
            return False, None

        frame = cv2.imread(
            self.files[self.index]
        )

        self.index += 1

        time.sleep(self.delay)

        return True, frame