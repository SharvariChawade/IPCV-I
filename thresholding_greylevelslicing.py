import cv2
import numpy as np

img1 = cv2.imread('image.jpg')

grey_img1 = cv2.imread('image.jpg',0)
h,w = grey_img1.shape

# Digital Negative
neg_img = 255 - grey_img1

# Thresholding
t = 50
i = 0
j = 0
threshold_img = np.zeros((h,w))
for i in range(h):
    for j in range(w):
        if grey_img1[i][j]>t:
            threshold_img[i][j] = 255
        else:
            threshold_img[i][j] = 0

# Grey level Slicing with BG
a = 150
b = 175
i = 0
j = 0
wbg_img = np.zeros((h,w),np.uint8)
for i in range(h):
    for j in range(w):
        r = grey_img1[i][j]
        if (grey_img1[i][j]>=a and grey_img1[i][j]<=b):
            wbg_img[i][j] = 255
        else:
            wbg_img[i][j] = r

# Grey level Slicing without BG
a = 150
b = 175
i = 0
j = 0
wobg_img = np.zeros((h,w))
for i in range(h):
    for j in range(w):
        if (grey_img1[i][j]>=a and grey_img1[i][j]<=b):
            wobg_img[i][j] = 255
        else:
            wobg_img[i][j] = 0

cv2.imshow('Negative',neg_img)
cv2.waitKey()

cv2.imshow('Threshold Image',threshold_img)
cv2.waitKey()

cv2.imshow('Grey Level Sliced with Background Image',wbg_img)
cv2.waitKey()

cv2.imshow('Grey Level Sliced without Background Image',wobg_img)
cv2.waitKey()