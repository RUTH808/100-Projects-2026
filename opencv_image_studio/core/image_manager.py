import cv2


class ImageManager:

    def __init__(self):

        self.original = None
        self.current = None
        self.path = None

    def load(self, path):

        self.path = path

        image = cv2.imread(path)

        if image is None:
            raise ValueError(
                f"Unable to load image: {path}"
            )

        self.original = image

        self.current = image.copy()

    def reset(self):

        if self.original is not None:

            self.current = (
                self.original.copy()
            )

    def save(self, path):

        if self.current is None:
            return

        cv2.imwrite(
            path,
            self.current
        )