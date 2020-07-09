import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('roi.jpg')
cv.imshow('img',img)


'''
ball=img[280:340,330:390]
img[273:333,100:160]= ball
cv.imshow('img2',img)
'''
