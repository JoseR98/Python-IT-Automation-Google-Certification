#!/usr/bin/python3
""" Change characteristics for images inside images folder.
Characteristics to change:
- size
- rotation
- convert from .tiff to JPEG format """

import os
from PIL import Image

for img in os.listdir('/images'):
    if not img.startswith('.') and not img.endswith('.py'):
        im = Image.open(img).rotate(90).resize((128, 128)).convert('RGB').save('/opt/icons/' + str(img) + '.jpeg')

