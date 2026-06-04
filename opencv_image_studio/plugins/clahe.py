import cv2

PLUGIN_NAME = "CLAHE"

PLUGIN_PARAMS = {

    "Clip Limit": {

        "min": 1,
        "max": 10,
        "default": 2
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

    clahe = cv2.createCLAHE(

        clipLimit=float(
            params["Clip Limit"]
        ),

        tileGridSize=(8, 8)
    )

    return clahe.apply(
        gray
    )