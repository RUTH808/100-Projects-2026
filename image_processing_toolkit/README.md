Project Overview

The OpenCV Image Processing Toolkit is a modular desktop application designed to demonstrate and perform fundamental and intermediate image processing techniques using OpenCV. The project provides a user-friendly graphical interface where users can select images from a predefined dataset, apply different image enhancement and transformation operations, visualize the results in real time, and save the processed output.

The primary objective of this project is to create an interactive environment for learning, experimenting with, and understanding image processing concepts without requiring users to write OpenCV code manually.

Key Features
Image Loading System

The application automatically scans a designated data/ directory and loads all supported image formats, including:

JPG
JPEG
PNG
BMP

Users can select any image from the image list displayed in the interface.

Image Conversion Operations

The toolkit supports image format and color-space transformations such as:

Grayscale Conversion

Converts a color image into a single-channel grayscale image by removing color information while preserving intensity information.

Grayscale to Color Conversion

Converts grayscale images back into a 3-channel image format to enable operations that require multiple channels.

Filtering and Enhancement

Several image enhancement techniques are included:

Gaussian Blur

Reduces image noise and detail using a Gaussian kernel.

Applications:

Noise reduction
Preprocessing for edge detection
Image smoothing
Average Blur

Applies uniform averaging across neighboring pixels.

Median Blur

Removes salt-and-pepper noise while preserving edges better than average blur.

Sharpening

Enhances edges and image details using convolution kernels.

Unblurring

Uses sharpening filters to restore some lost detail from blurred images.

Edge and Feature Detection
Canny Edge Detection

Identifies object boundaries and significant intensity changes within an image.

Useful for:

Object recognition
Shape detection
Computer vision preprocessing
Image Segmentation
Thresholding

Converts grayscale images into binary images by separating pixels into foreground and background categories.

Applications:

Document scanning
OCR preprocessing
Object extraction
Contrast Enhancement
Histogram Equalization

Improves image contrast by redistributing pixel intensity values.

Useful for:

Low-light images
Medical imaging
Surveillance footage
Brightness and Contrast Control
Brightness Adjustment

Increases image illumination using HSV color-space manipulation.

Contrast Adjustment

Improves distinction between light and dark regions through pixel intensity scaling.

Geometric Transformations
Rotation

Rotates images around their center by a specified angle.

Horizontal Flip

Creates a mirror image along the vertical axis.

Vertical Flip

Flips the image along the horizontal axis.

Resize

Changes image dimensions to user-defined resolutions.

Noise Operations
Noise Addition

Introduces synthetic Gaussian noise for testing image restoration algorithms.

Denoising

Uses OpenCV's Non-Local Means algorithm to remove noise while preserving important image structures.

Image Preview System

The application provides real-time visual feedback using:

Tkinter GUI
Pillow image rendering
Dynamic image updates

Users can immediately observe the effects of each operation without saving files.

Output Management

Processed images can be saved automatically to an output/ directory.

Output files are generated with modified filenames to preserve original images.

Example:
