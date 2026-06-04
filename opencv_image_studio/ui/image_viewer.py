from PIL import Image
from PIL import ImageTk
import cv2


class ImageViewer:

    zoom_factor = 1.0

    @staticmethod
    def zoom_in():

        ImageViewer.zoom_factor *= 1.2

    @staticmethod
    def zoom_out():

        ImageViewer.zoom_factor /= 1.2

        if ImageViewer.zoom_factor < 0.2:
            ImageViewer.zoom_factor = 0.2

    @staticmethod
    def fit():

        ImageViewer.zoom_factor = 1.0

    @staticmethod
    def convert(img):

        if img is None:
            return None

        if len(img.shape) == 2:

            img = cv2.cvtColor(
                img,
                cv2.COLOR_GRAY2RGB
            )

        else:

            img = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2RGB
            )

        pil = Image.fromarray(img)

        width = int(
            pil.width *
            ImageViewer.zoom_factor
        )

        height = int(
            pil.height *
            ImageViewer.zoom_factor
        )

        width = max(width, 1)
        height = max(height, 1)

        pil = pil.resize(
            (width, height)
        )

        if width > 700 or height > 700:

            pil.thumbnail(
                (700, 700)
            )

        return ImageTk.PhotoImage(
            pil
        )