import qrcode
import random
import string
import os

os.makedirs("images", exist_ok=True)

for i in range(50):
    text = ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=20
        )
    )

    qrcode.make(text).save(f"images/qr_{i}.png")

print("Generated 50 QR codes.")