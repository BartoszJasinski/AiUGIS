import sys
import numpy as np
import cv2

# loading image
img = cv2.imread('brodno.png', 1)

# color system conversion
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# epsilon on color pick error
sensitivity = 20

# color green range
lower_range = np.array([36, 0, 0], dtype=np.uint8)
upper_range = np.array([70, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, (36 - sensitivity, 40, 0), (70 + sensitivity, 255, 255))
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('res', res)
cv2.imshow('image', img)

while (1):
    k = cv2.waitKey(0)
    if k == 27:
        break

cv2.destroyAllWindows()
