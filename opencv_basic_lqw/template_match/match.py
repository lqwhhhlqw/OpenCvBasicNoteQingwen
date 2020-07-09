import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img_original = cv.imread('cat.jpg', 0)
img2 = img_original.copy()
popcorn = cv.imread('popcorn.jpg', 0)
width, height = popcorn.shape[::-1]

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)
    res = cv.matchTemplate(img, popcorn, method)
    min_value, max_value, min_location, max_location = cv.minMaxLoc(res)

    '''最佳匹配值此情况下为全局最小值  (列/宽，行/高）'''

    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_location
    else:
        top_left = max_location

    bottom_right = top_left[0] + width, top_left[1] + height
    cv.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title(' match result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title(' detected img'), plt.xticks([]), plt.yticks([])
    plt.show()
