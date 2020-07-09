import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

img = cv.imread('ke.jpeg', 0)
row, col = img.shape
crow, ccol = row // 2, col // 2

'''f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

fshift[crow - 30:crow + 31, ccol - 30:ccol + 31] = 0

f_ishift = np.fft.ifftshift(fshift)

img_back = np.fft.ifft2(f_ishift)

img_back = np.real(img_back)

plt.subplot(121), plt.title("high pass filtering"), plt.imshow(img_back)
plt.subplot(122), plt.title("original"), plt.imshow(img,cmap='gray')
plt.show()
'''

# remove high frequency contents in the image

dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

mask = np.zeros((row, col, 2), np.uint8)
mask[crow - 30:crow + 31, ccol - 30:ccol + 31] = 1

fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv.idft(f_ishift)
img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1]) #??作用

plt.subplot(121), plt.title("low pass filtering"), plt.imshow(img_back,)
plt.subplot(122), plt.title("original"), plt.imshow(img, cmap='gray')
plt.show()



'''
时间可以减少
'''