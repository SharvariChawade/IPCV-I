import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

img = cv2.imread('images.jpeg',0)

h,w = img.shape

F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)

H = np.zeros((h,w),dtype = np.float32)
D0 = 50

for i in range(h):
    for j in range(w):
        D = np.sqrt((i-h/2)**2 + (j-w/2)**2)
        if D<D0:
            H[i][j] = 1
        else:
            H[i][j] = 0

Gshift = Fshift * H

#ideal high pass
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

cv2.imshow("H", H)
cv2.waitKey()

plt.imshow(g,cmap='gray')
plt.show()

#ideal low pass
H = 1-H
Gshift = Fshift * H

G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))

plt.imshow(g,cmap='gray')
plt.show()