#! /usr/bin/env python3

"""
Iterate through each image to rotate, resize, and save image in a different format.

Author: AlperHuseyn:wq:w
Date: 29/03/2023
"""

from PIL import Image
import os

# Path contains the images
inp_folder = os.getcwd() + '/images/'
# Path to images to be saved
out_folder = '/opt/icons/'

# Iterate through each file into the path
for fname in os.listdir(inp_folder):
    # Ignore hidden file (images/.DS_Store)
    if fname.startswith('ic_'):
        with Image.open(inp_folder + fname) as img:
            img.rotate(270).resize((128, 128)).convert('RGB').save(out_folder + fname, format='JPEG')
