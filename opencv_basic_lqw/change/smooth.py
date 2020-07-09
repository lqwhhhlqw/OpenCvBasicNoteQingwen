import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('cat.jpg')
kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)

blur = cv.blur(img, (5, 5))
blur_Gausssain = cv.GaussianBlur(img, (5, 5), 0)

#median It reduces the noise effectively.
median=cv.medianBlur(img,5)


# it preserves the edges
blur_bilateral=cv.bilateralFilter(img,9,300,300)



plt.subplot(321), plt.imshow(img), plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(322), plt.imshow(blur), plt.title('averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(323), plt.imshow(blur_Gausssain), plt.title('gaussian')
plt.xticks([]), plt.yticks([])
plt.subplot(324), plt.imshow(dst), plt.title('filter2D')
plt.xticks([]), plt.yticks([])
plt.subplot(325), plt.imshow(median), plt.title('Median')
plt.xticks([]), plt.yticks([])
plt.subplot(326), plt.imshow(blur_bilateral), plt.title('bilateralFilter')
plt.xticks([]), plt.yticks([])
plt.show()
