#!/usr/bin/python3
"""Upload images to the server"""

import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = 'http://localhost/upload/'
for img in os.listdir('supplier-data/images/'):
  if img.endswith('.jpeg'):
    with open('supplier-data/images/{}'.format(img), 'rb') as opened:
      r = requests.post(url, files={'file': opened})
