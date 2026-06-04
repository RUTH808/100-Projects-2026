import cv2

PLUGIN_NAME = "Sketch"

PLUGIN_PARAMS = {}


def process(img, params):

    if len(img.shape) == 3:

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

    else:

        gray = img

    inverted = 255 - gray

    blur = cv2.GaussianBlur(
        inverted,
        (21, 21),
        0
    )

    inverted_blur = (
        255 - blur
    )

    sketch = cv2.divide(
        gray,
        inverted_blur,
        scale=256
    )

    return sketch