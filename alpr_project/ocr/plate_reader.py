import cv2
import pytesseract
import re

# Update path if necessary
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class PlateReader:

    def read(self, plate):

        gray = cv2.cvtColor(
            plate,
            cv2.COLOR_BGR2GRAY
        )

        gray = cv2.resize(
            gray,
            None,
            fx=3,
            fy=3
        )

        gray = cv2.GaussianBlur(
            gray,
            (3, 3),
            0
        )

        _, thresh = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY +
            cv2.THRESH_OTSU
        )

        text = pytesseract.image_to_string(
            thresh,
            config=(
                "--oem 3 "
                "--psm 7 "
                "-c tessedit_char_whitelist="
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            )
        )

        text = re.sub(
            r'[^A-Z0-9]',
            '',
            text.upper()
        )

        return text