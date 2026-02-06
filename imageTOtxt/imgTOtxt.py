import pytesseract
from PIL import Image
import os

def convert():
    img = Image.open("imagee.jpg")
    text = pytesseract.image_to_string(img)
    print(text)
    
convert()
