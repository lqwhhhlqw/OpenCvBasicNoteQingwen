import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def nothing(x):
    pass


# find edge of the image
img = cv.imread("cat.jpg",0)

# trackbar and window
cv.namedWindow('cat')
switch = '0:OFF \n1: On'
cv.createTrackbar(switch, 'cat', 0, 1, nothing)
cv.createTrackbar('min', 'cat', 0, 255, nothing)
cv.createTrackbar('max', 'cat', 0, 255, nothing)

while (1):
    min = cv.getTrackbarPos('min', 'cat')
    max = cv.getTrackbarPos('max', 'cat')
    s = cv.getTrackbarPos(switch, 'cat')

    if s == 0:
        edge = img
    else:
        edge = cv.Canny(img, min, max)
    cv.imshow('original',img)
    cv.imshow('canny edge',edge)
    k = cv.waitKey(1) & 0xFF
    if k == 27:   # hit escape to quit
        break

cv.destroyAllWindows()


'''
plt.subplot(121), plt.imshow(img), plt.title("original")

plt.subplot(122), plt.imshow(edge), plt.title("edge")
plt.show()
'''
