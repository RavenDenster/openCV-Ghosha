import pytesseract
import cv2
from PIL import Image

img = Image.open('number.png')
pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, lang='eng', config=custom_config)
print(text)