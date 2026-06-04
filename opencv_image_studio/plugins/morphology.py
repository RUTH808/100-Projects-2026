import cv2
import numpy as np

PLUGIN_NAME = "Morphology"

PLUGIN_PARAMS = {

    "Kernel Size": {

        "min": 1,
        "max": 25,
        "default": 5
    }
}


def process(img, params):

    k = int(
        params["Kernel Size"]
    )

    kernel = np.ones(
        (k, k),
        np.uint8
    )

    return cv2.morphologyEx(

        img,

        cv2.MORPH_OPEN,

        kernel
    )