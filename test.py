import time
from PIL import ImageGrab  # screenshot

import pytesseract
from pytesseract import Output
print("start")
time.sleep(2)
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe") # needed for Windows as OS

screen =  ImageGrab.grab(region=(100,180, 300, 400))  # screenshot
cap = screen.convert('L')   # make grayscale

data=pytesseract.image_to_boxes(cap,output_type=Output.DICT)

print(data)