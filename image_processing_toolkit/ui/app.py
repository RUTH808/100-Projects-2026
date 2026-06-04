import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

from processing.image_operations import ImageProcessor
from utils.file_utils import (
    load_images,
    save_image
)


class ImageProcessingApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "OpenCV Image Processing Toolkit"
        )

        self.root.geometry("1200x700")

        self.images = load_images("data")

        self.current_name = None
        self.current_image = None

        self.create_widgets()

    def create_widgets(self):

        left_frame = tk.Frame(self.root)
        left_frame.pack(
            side=tk.LEFT,
            fill=tk.Y,
            padx=10
        )

        self.listbox = tk.Listbox(
            left_frame,
            width=30
        )

        self.listbox.pack(fill=tk.Y)

        for img_name in self.images:
            self.listbox.insert(
                tk.END,
                img_name
            )

        self.listbox.bind(
            "<<ListboxSelect>>",
            self.load_selected
        )

        operations = [
            "Grayscale",
            "RGB",
            "Gaussian Blur",
            "Average Blur",
            "Median Blur",
            "Sharpen",
            "Unblur",
            "Edge Detection",
            "Threshold",
            "Histogram Equalization",
            "Brightness",
            "Contrast",
            "Rotate",
            "Flip Horizontal",
            "Flip Vertical",
            "Noise",
            "Denoise"
        ]

        self.operation = ttk.Combobox(
            left_frame,
            values=operations
        )

        self.operation.pack(
            pady=10
        )

        tk.Button(
            left_frame,
            text="Apply",
            command=self.apply_operation
        ).pack(pady=5)

        tk.Button(
            left_frame,
            text="Save Output",
            command=self.save_output
        ).pack(pady=5)

        self.image_label = tk.Label(self.root)

        self.image_label.pack(
            side=tk.RIGHT,
            expand=True
        )

    def load_selected(self, event):

        idx = self.listbox.curselection()

        if not idx:
            return

        self.current_name = self.listbox.get(
            idx
        )

        self.current_image = self.images[
            self.current_name
        ]

        self.show_image(
            self.current_image
        )

    def show_image(self, img):

        if len(img.shape) == 2:
            display_img = cv2.cvtColor(
                img,
                cv2.COLOR_GRAY2RGB
            )
        else:
            display_img = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2RGB
            )

        pil_img = Image.fromarray(
            display_img
        )

        pil_img.thumbnail((800, 600))

        photo = ImageTk.PhotoImage(
            pil_img
        )

        self.image_label.configure(
            image=photo
        )

        self.image_label.image = photo

    def apply_operation(self):

        op = self.operation.get()

        if self.current_image is None:
            return

        processor = ImageProcessor

        operations_map = {
            "Grayscale":
                processor.to_grayscale,

            "RGB":
                processor.to_rgb,

            "Gaussian Blur":
                processor.gaussian_blur,

            "Average Blur":
                processor.average_blur,

            "Median Blur":
                processor.median_blur,

            "Sharpen":
                processor.sharpen,

            "Unblur":
                processor.unblur,

            "Edge Detection":
                processor.edge_detection,

            "Threshold":
                processor.threshold,

            "Histogram Equalization":
                processor.histogram_equalization,

            "Brightness":
                processor.increase_brightness,

            "Contrast":
                processor.adjust_contrast,

            "Rotate":
                processor.rotate,

            "Flip Horizontal":
                processor.flip_horizontal,

            "Flip Vertical":
                processor.flip_vertical,

            "Noise":
                processor.add_noise,

            "Denoise":
                processor.denoise,
        }

        self.current_image = operations_map[
            op
        ](self.current_image)

        self.show_image(
            self.current_image
        )

    def save_output(self):

        if self.current_image is None:
            return

        save_image(
            self.current_image,
            "output",
            f"processed_{self.current_name}"
        )

