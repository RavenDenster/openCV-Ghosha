import cv2
import numpy 

photo = cv2.imread("img/tyn.jpg")
img = numpy.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (430,330), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=circle)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(square)

cv2.imshow('Result', img)
cv2.waitKey(0)