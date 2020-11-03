#!/usr/bin/env python3
"""Send post request for each description inside descriptions folder"""

import os
import requests

for fruit in os.listdir('supplier-data/descriptions/'):
  if fruit.endswith('.txt'):
    with open('supplier-data/descriptions/{}'.format(fruit)) as opened:
      info = opened.read().split('\n')
      name = info[0]
      weight = int(info[1].strip('lbs'))
      description = info[2]
      image_name = fruit.strip('.txt') + '.jpeg'
      img = fruit.strip('.txt')
      new_info = {"name": name, "weight": weight, "description": description, "image_name": image_name}
      r = requests.post("http://localhost/fruits/", json=new_info)
      print(r.status_code)
