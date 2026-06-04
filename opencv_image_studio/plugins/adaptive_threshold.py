import cv2

PLUGIN_NAME = "Adaptive Threshold"

PLUGIN_PARAMS = {

    "Block Size": {

        "min": 3,
        "max": 51,
        "default": 11
    }
}


def process(img, params):

    if len(img.shape) == 3:

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

    else:

        gray = img

    block = int(
        params["Block Size"]
    )

    if block % 2 == 0:
        block += 1

    return cv2.adaptiveThreshold(

        gray,

        255,

        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,

        cv2.THRESH_BINARY,

        block,

        2
    )