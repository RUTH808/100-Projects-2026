import cv2

PLUGIN_NAME = "Grayscale"

PLUGIN_PARAMS = {}


def process(img, params):

    if len(img.shape) == 2:
        return img

    return cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )