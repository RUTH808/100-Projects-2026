import cv2

PLUGIN_NAME = "Cartoon"

PLUGIN_PARAMS = {

    "Blur": {

        "min": 3,
        "max": 15,
        "default": 7
    }
}


def process(img, params):

    blur_size = int(
        params["Blur"]
    )

    if blur_size % 2 == 0:
        blur_size += 1

    gray = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2GRAY
    )

    gray = cv2.medianBlur(
        gray,
        blur_size
    )

    edges = cv2.adaptiveThreshold(

        gray,

        255,

        cv2.ADAPTIVE_THRESH_MEAN_C,

        cv2.THRESH_BINARY,

        9,

        9
    )

    color = cv2.bilateralFilter(

        img,

        9,

        300,

        300
    )

    return cv2.bitwise_and(
        color,
        color,
        mask=edges
    )