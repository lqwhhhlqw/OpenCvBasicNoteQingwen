import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('water_coins.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

# opening  and closing morphologyEx
kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv.dilate(opening, kernel, iterations=3)

# sure fg
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# find unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)

# make label (bg--0, objects:1,2,3...)
ret, markers = cv.connectedComponents(sure_fg)
markers = markers + 1  # all known label of sur bg  is 1, to differ with unkonwn region which we define as 0
markers[unknown == 255] = 0
markers = cv.watershed(img, markers)  # find boundary
img[markers == -1] = [255, 0, 0]

plt.subplot(221), plt.imshow(img), plt.title("result")
plt.subplot(222), plt.imshow(markers), plt.title("markers img")
plt.subplot(223), plt.imshow(sure_fg), plt.title("sure_foreground img")
plt.show()
