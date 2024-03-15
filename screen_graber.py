from PIL import ImageGrab, ImageOps, Image
from screeninfo import get_monitors
from colormap import rgb2hex
import os
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import random

def get_resolution():
    on_primary = True            #TODO choose if primary od sec..
    resolution = (1,1)
    for m in get_monitors():
        print(m.width , m.height)
        if m.is_primary and on_primary:
            resolution = (m.width, m.height)
        elif not m.is_primary and not on_primary:
            resolution = (m.width, m.height)
    return resolution

def screen_grab():
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full__snap' + '.png', 'PNG')
    return im

def get_color_pixel(x,y):
    im = screen_grab()
    coordinate = x, y
    rgb = im.getpixel(coordinate)
                        #TODO nejde hodit tuple do rgb2hex
    hex = rgb2hex(rgb[0],rgb[1],rgb[2])
    return hex

def crop_image(img, frameTuple):
    croppedImg = img.crop(frameTuple)
    croppedImg.save(os.getcwd() + '\\cropped__snap' + '.png', 'PNG')
    return croppedImg

def get_text(img):
    img = Image.open('cropped__snap.png').convert('RGB')
    img = ImageOps.invert(img)
    text = pt.image_to_string(img)
    return text
