import cv2
import os
import csv

# Folder containing images
IMAGE_FOLDER = "images"

# Output CSV file
OUTPUT_FILE = "qr_results.csv"

# Create QR detector
detector = cv2.QRCodeDetector()

results = []

# Scan all images in folder
for filename in os.listdir(IMAGE_FOLDER):

    if not filename.lower().endswith(
        (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
    ):
        continue

    image_path = os.path.join(IMAGE_FOLDER, filename)

    image = cv2.imread(image_path)

    if image is None:
        print(f"Could not read {filename}")
        continue

    # Detect and decode QR code
    data, points, _ = detector.detectAndDecode(image)

    if data:
        print(f"[FOUND] {filename} -> {data}")
        results.append([filename, data])
    else:
        print(f"[NONE ] {filename}")
        results.append([filename, "NO_QR_FOUND"])

# Save results
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([
        "image_name",
        "decoded_qr"
    ])

    writer.writerows(results)

print(f"\nResults saved to {OUTPUT_FILE}")