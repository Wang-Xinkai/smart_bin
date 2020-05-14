from django.shortcuts import render
import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageEnhance
# test code
img = Image.open("/Users/wangxinkai/Desktop/1.png")
texts = pyzbar.decode(img)
for text in texts:
    tt = text.data.decode("utf-8")
    print(tt)

# Create your views here.
