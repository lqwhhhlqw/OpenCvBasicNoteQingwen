import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

roi = cv.imread('roi.jpg')
col, row, cal = roi.shape

img_two = cv.imread('logo.jpg')
logo = img_two[0:col, 0:row]
# dst = cv.addWeighted(roi, 0.7, logo, 0.3, 0)
logoGray = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)

ret, mask = cv.threshold(logoGray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

roi_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
logo_fg = cv.bitwise_and(logo, logo, mask=mask)

dst = cv.bitwise_and(roi_bg, logo_fg)

cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()
