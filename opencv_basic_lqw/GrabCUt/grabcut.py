import numpy as np
from matplotlib import  pyplot as plt
import cv2 as cv

img = cv.imread('messi.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

fgdModel = np.zeros((1, 65), np.float64)
bgdModel = np.zeros((1, 65), np.float64)

rect = (50, 50, 400, 280)

cv.grabCut(img, mask, rect, fgdModel, bgdModel, 5, cv.GC_INIT_WITH_RECT)

maskNew = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

img = img * maskNew[:, :, np.newaxis]

plt.imshow(img), plt.colorbar(), plt.show()
