import cv2
import numpy as np

PLUGIN_NAME = "Sharpen"

PLUGIN_PARAMS = {

    "Strength": {

        "min": 1,
        "max": 10,
        "default": 3
    }
}


def process(img, params):

    strength = int(
        params["Strength"]
    )

    kernel = np.array([

        [0, -1, 0],
        [-1, 5 + strength, -1],
        [0, -1, 0]

    ])

    return cv2.filter2D(
        img,
        -1,
        kernel
    )