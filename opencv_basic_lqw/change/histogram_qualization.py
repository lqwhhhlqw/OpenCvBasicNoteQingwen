import numpy as np
import cv2 as cv

img = cv.imread('clahe.jpg', 0)

clahe = cv.createCLAHE(clipLimit=40, tileGridSize=(8, 8))
cll = clahe.apply(img)

cv.imwrite('clahe2.jpg', cll)
