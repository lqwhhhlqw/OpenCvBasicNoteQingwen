import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('coin.jpg',0)
plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
'''
cv.namedWindow('image',cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
'''

