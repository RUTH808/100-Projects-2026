import cv2
import numpy as np


class ImageProcessor:

    @staticmethod
    def to_grayscale(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def to_rgb(img):
        if len(img.shape) == 2:
            return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    @staticmethod
    def gaussian_blur(img, ksize=11):
        return cv2.GaussianBlur(img, (ksize, ksize), 0)

    @staticmethod
    def average_blur(img, ksize=11):
        return cv2.blur(img, (ksize, ksize))

    @staticmethod
    def median_blur(img, ksize=5):
        return cv2.medianBlur(img, ksize)

    @staticmethod
    def sharpen(img):
        kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ])
        return cv2.filter2D(img, -1, kernel)

    @staticmethod
    def edge_detection(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 100, 200)

    @staticmethod
    def threshold(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(
            gray, 127, 255, cv2.THRESH_BINARY
        )
        return thresh

    @staticmethod
    def histogram_equalization(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.equalizeHist(gray)

    @staticmethod
    def increase_brightness(img, value=40):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        h, s, v = cv2.split(hsv)

        v = np.clip(v + value, 0, 255)

        hsv = cv2.merge([h, s, v.astype(np.uint8)])

        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    @staticmethod
    def adjust_contrast(img, alpha=1.5):
        return cv2.convertScaleAbs(img, alpha=alpha)

    @staticmethod
    def rotate(img, angle=90):
        h, w = img.shape[:2]

        center = (w // 2, h // 2)

        matrix = cv2.getRotationMatrix2D(
            center,
            angle,
            1.0
        )

        return cv2.warpAffine(img, matrix, (w, h))

    @staticmethod
    def flip_horizontal(img):
        return cv2.flip(img, 1)

    @staticmethod
    def flip_vertical(img):
        return cv2.flip(img, 0)

    @staticmethod
    def resize(img, width=500, height=500):
        return cv2.resize(img, (width, height))

    @staticmethod
    def add_noise(img):
        noise = np.random.normal(
            0,
            25,
            img.shape
        ).astype(np.uint8)

        return cv2.add(img, noise)

    @staticmethod
    def denoise(img):
        return cv2.fastNlMeansDenoisingColored(
            img,
            None,
            10,
            10,
            7,
            21
        )

    @staticmethod
    def unblur(img):
        sharpen_kernel = np.array([
            [-1,-1,-1],
            [-1, 9,-1],
            [-1,-1,-1]
        ])

        return cv2.filter2D(
            img,
            -1,
            sharpen_kernel
        )