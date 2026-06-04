import os
import cv2


def load_images(folder_path):
    images = {}

    for file in os.listdir(folder_path):

        if file.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp")
        ):
            path = os.path.join(folder_path, file)

            images[file] = cv2.imread(path)

    return images


def save_image(img, output_folder, filename):

    os.makedirs(output_folder, exist_ok=True)

    path = os.path.join(
        output_folder,
        filename
    )

    cv2.imwrite(path, img)