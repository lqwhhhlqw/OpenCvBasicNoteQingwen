import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('blox.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
corner = cv.goodFeaturesToTrack(gray, 25, 0.1, 0.01)
corner = np.int0(corner)

for i in corner:
    x, y = i.ravel()
cv.circle(img, (x, y), 3, 255, -1)

plt.imshow(img), plt.show()
