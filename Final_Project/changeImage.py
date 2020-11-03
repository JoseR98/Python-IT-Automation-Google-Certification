#!/usr/bin/python3
"""Modify Images inside supplier-data/images folder"""

import os
from PIL import Image

for img in os.listdir('supplier-data/images'):
  if img.endswith('.tiff'):
    img_name = img[:-5]
    im = Image.open('supplier-data/images/' + img).resize((600, 400)).convert('RGB').save('supplier-data/images/' + img_name + '.jpeg')
