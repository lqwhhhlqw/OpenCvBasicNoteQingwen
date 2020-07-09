import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while (1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    lower_green = np.array([50, 50, 120])
    upper_green = np.array([70, 255, 255])

    b_mask = cv.inRange(hsv, lower_blue, upper_blue)
    g_mask = cv.inRange(hsv, lower_green, upper_green)
    mask = b_mask + g_mask
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
