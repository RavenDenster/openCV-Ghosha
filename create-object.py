import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')
# photo[:] = 119, 201, 105 # [:] - обращение ко всем элемента массива
# photo[100:150, 200:280] = 119, 201, 105

cv2.rectangle(photo, (100, 100), (200, 200), (119, 201, 105), thickness=3)

cv2.line(photo, (0, photo.shape[0] // 2), (100, photo.shape[0] // 2), (119, 201, 105), thickness=3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 100, (119, 201, 105), thickness=cv2.FILLED)

cv2.putText(photo, 'Hey, pidor', (50, 350), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 0), thickness=2)

cv2.imshow('Photo', photo)
cv2.waitKey(0)