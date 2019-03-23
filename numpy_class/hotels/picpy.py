from PIL import Image
from pytesseract import image_to_string
import os
print (image_to_string(Image.open("pic.jpg")))
print (image_to_string(Image.open("unipage.pdf"), lang='eng'))