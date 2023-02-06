from PIL import Image
from pytesseract import pytesseract



def main():
    result = ImgToText()
    Interaction(result)

def ImgToText():
    #Define path to tessaract.exe
    #path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    #Define path to image
    path_to_image = 'images/p3.png'


    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)

    #Extract text from image
    text = pytesseract.image_to_string(img)
    result = text.split()

    #print result
    print(result)
    return result

def Interaction(a):
    print(a[0])
