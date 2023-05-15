import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

img = cv2.imread('images.jpeg',0)
h,w = img.shape

F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)

D0 = 50
o = 2

# butterworth low pass 
H = np.zeros((h,w),dtype = np.float32)
for i in range(h):
    for j in range(w):
        D = np.sqrt((i-h/2)**2 + (j-w/2)**2)
        H[i][j] = 1/(1+(D/D0)**(2*o))

cv2.imshow('H',H)
cv2.waitKey()

Gshift = Fshift * H

G = np.fft.ifftshift(Gshift)
g = np.abs((np.fft.ifft2(G)))

plt.imshow(g,cmap='gray')
plt.show()

# butterworth high pass 
H = np.zeros((h,w),dtype = np.float32)
for i in range(h):
    for j in range(w):
        D = np.sqrt((i-h/2)**2 + (j-w/2)**2)
        H[i][j] = 1/(1+(D0/D)**o)

cv2.imshow('H',H)
cv2.waitKey()

Gshift = Fshift * H

G = np.fft.ifftshift(Gshift)
g = np.abs((np.fft.ifft2(G)))

plt.imshow(g,cmap='gray')
plt.show()