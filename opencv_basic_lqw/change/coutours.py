import numpy as np
import cv2 as cv

img = cv.imread('cat.jpg')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 170, 255, 0)
coutours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, coutours, -1, (0, 255, 0), 3)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()

'''
cnt=coutours[4]
cv.drawContours(img,[cnt],0,(0,255,0),3)
'''


