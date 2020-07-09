import numpy as np
import cv2 as cv

img = cv.imread('cat.jpg')
res = cv.resize(img, None, fx=3, fy=2, interpolation=cv.INTER_CUBIC)


cv.imshow('img',res)
cv.waitKey(0)
cv.destroyAllWindows()