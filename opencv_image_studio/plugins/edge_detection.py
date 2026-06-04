import cv2

PLUGIN_NAME = "Edge Detection"

PLUGIN_PARAMS = {

    "Threshold 1": {

        "min": 0,
        "max": 255,
        "default": 100
    },

    "Threshold 2": {

        "min": 0,
        "max": 255,
        "default": 200
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

    t1 = int(
        params["Threshold 1"]
    )

    t2 = int(
        params["Threshold 2"]
    )

    return cv2.Canny(
        gray,
        t1,
        t2
    )