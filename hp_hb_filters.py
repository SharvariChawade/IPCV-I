import cv2
import numpy as np

img = cv2.imread('image.jpg',0)
h,w = img.shape

cv2.imshow('Original image',img)
cv2.waitKey()

# high pass filter

mask = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

hp_img = np.zeros((h,w),np.uint8)

for i in range(h-1):
    for j in range(w-1):
        temp = img[i-1][j-1]*mask[0][0] + img[i-1][j]*mask[0][1] + img[i-1][j+1]*mask[0][2] + img[i][j-1]*mask[1][0] + img[i][j]*mask[1][1] + img[i][j+1]*mask[1][2] + img[i+1][j-1]*mask[2][0] + img[i+1][j]*mask[2][1] + img[i+1][j+1]*mask[2][2]
        hp_img[i][j] = temp

cv2.imshow('Image after high pass filtering',hp_img)
cv2.waitKey()

# high boost filter

a = 1.1
mask = np.array([[-1,-1,-1],[-1,8+a,-1],[-1,-1,-1]])

hb_img = np.zeros((h,w),np.uint8)

for i in range(h-1):
    for j in range(w-1):
        temp = img[i-1][j-1]*mask[0][0] + img[i-1][j]*mask[0][1] + img[i-1][j+1]*mask[0][2] + img[i][j-1]*mask[1][0] + img[i][j]*mask[1][1] + img[i][j+1]*mask[1][2] + img[i+1][j-1]*mask[2][0] + img[i+1][j]*mask[2][1] + img[i+1][j+1]*mask[2][2]
        hb_img[i][j] = temp

cv2.imshow('Image after high boost filtering',hb_img)
cv2.waitKey()