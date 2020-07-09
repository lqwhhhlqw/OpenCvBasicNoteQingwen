import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('j.png')
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)
# erosion and dilation to remove noise
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)



#dilation followed by erosion
closing=cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)


#outline
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)


#
plt.subplot(331), plt.imshow(img), plt.title("original")
plt.subplot(332), plt.imshow(erosion), plt.title("erosion")
plt.subplot(333), plt.imshow(dilation), plt.title("dilation")
plt.subplot(334), plt.imshow(opening), plt.title("morphology remove noises")
plt.subplot(335), plt.imshow(closing), plt.title("morphology closing holes")
plt.show()
