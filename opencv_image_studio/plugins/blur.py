import cv2

PLUGIN_NAME = "Gaussian Blur"

PLUGIN_PARAMS = {

    "Kernel Size": {

        "min": 1,
        "max": 51,
        "default": 9
    }
}


def process(img, params):

    k = int(
        params["Kernel Size"]
    )

    if k % 2 == 0:
        k += 1

    return cv2.GaussianBlur(
        img,
        (k, k),
        0
    )