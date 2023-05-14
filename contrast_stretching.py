import cv2
import numpy as np
import math

img = cv2.imread('lcimg.jpeg',0)
h,w = img.shape

imax = img.max()
imin = img.min()



# log transformation

c = 50
log_img = np.zeros((h,w),np.uint8)
log_img2 = log_img
for i in range(h):
    for j in range(w):
        r = img[i][j]
        x = int(c * (math.log((r)+1)))
        log_img[i][j] = x

cv2.imshow('Log transformed image', log_img)
cv2.waitKey(0)

# power transformation

g = 1.1
power_img = np.zeros((h,w),np.uint8)

for i in range(h):
    for j in range(w):
        r = img[i][j]
        power_img[i][j] = int(r**g)

cv2.imshow('power transformed image', power_img)
cv2.waitKey(0)

#contrast stretching

print("Original image pixels: ",imax,imin)

a = 50
b = 150
l = 0.5
m = 2
n = 0.3
v = l*a
w = m*(b-a)+l*a
h,x = img.shape
stretched_img = np.zeros((h,x),np.uint8)

for i in range(h):
    for j in range(x):
        r = img[i][j]
        if(r>0 and r<=a):
            stretched_img[i][j] = int(l*r)
        elif(r>a and r<=b):
            stretched_img[i][j] = int(m*(r-a) + v)
        elif(r>b and r<=255):
            stretched_img[i][j] = int(n*(r-b) + w)

print(stretched_img.max(),stretched_img.min())
cv2.imshow('Contrast stretched image', stretched_img)
cv2.waitKey(0)