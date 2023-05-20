import cv2
import numpy as np
import imutils
from matplotlib import pyplot as pl
from PIL import Image

img = cv2.imread('img/auto-3.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15) # уменьшим шум (изображение, как много пикселей будет охвачено, как сильно будут смешиваться, смешивание по координатам)
edges = cv2.Canny(img_filter, 30, 200)

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # (изображение, все контуры в иерархии, находит только начальную и кон точку)
cont = imutils.grab_contours(cont) # список контуров
cont = sorted(cont, key=cv2.contourArea, reverse=True)

pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 10, True) # примерно квадрат (изоб, на сколько квадрат, только закрытые формы)

    if len(approx) == 4: # координаты углов
        pos = approx
        break

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropp = gray[x1:x2, y1:y2]

img = Image.fromarray(cropp, mode='L')
img.save('number.png')

pl.imshow(cv2.cvtColor(cropp, cv2.COLOR_BGR2RGB))
pl.show()