"""Read shipping-label barcodes from check-in photos.

Usage: python3 -I read_label.py photo1.jpg [photo2.jpg ...]
Needs: pip install zxing-cpp pillow

Prints one line per photo: the file name, then each tracking number found
with its carrier guess. A photo with no readable label prints "none".
"""
import re
import sys

import zxingcpp
from PIL import Image, ImageOps


def carrier(code):
    if code.startswith("TBA"):
        return "Amazon", code
    if code.startswith("1Z"):
        return "UPS", code
    m = re.fullmatch(r"420\d{5}(?:\d{4})?(9\d{19,21})", code)
    if m:  # USPS: strip the 420 + ZIP routing prefix
        return "USPS", m.group(1)
    if re.fullmatch(r"9\d{19,21}", code):
        return "USPS", code
    if re.fullmatch(r"\d{34}", code):  # FedEx Ground: tracking is the last 12
        return "FedEx", code[-12:]
    if re.fullmatch(r"\d{12}|\d{15}", code):
        return "FedEx", code
    return None, code


def barcodes(path):
    """Scan the whole photo, then overlapping tiles, so a small label still reads."""
    im = ImageOps.exif_transpose(Image.open(path)).convert("L")
    w, h = im.size
    boxes = [(0, 0, w, h)]
    for n in (2, 3):
        tw, th = w // n, h // n
        for i in range(n * 2 - 1):
            for j in range(n * 2 - 1):
                x, y = i * tw // 2, j * th // 2
                boxes.append((x, y, min(w, x + tw), min(h, y + th)))
    found = {}
    for box in boxes:
        tile = im.crop(box)
        for scale in (1, 0.5):
            t = tile.resize((max(1, int(tile.width * scale)), max(1, int(tile.height * scale))))
            for img in (t, ImageOps.autocontrast(t)):
                for r in zxingcpp.read_barcodes(img, try_rotate=True, try_downscale=True):
                    if "128" in str(r.format):
                        found.setdefault(r.text, None)
    return list(found)


for path in sys.argv[1:]:
    hits = [carrier(c) for c in barcodes(path)]
    hits = [f"{name} {num}" for name, num in hits if name]
    print(path.rsplit("/", 1)[-1], "|", "; ".join(hits) or "none")
