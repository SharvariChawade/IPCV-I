import cv2
import numpy as np

img = cv2.imread('image.jpg',0)
h,w = img.shape

cv2.imshow('Original image',img)
cv2.waitKey()

# prewitts

px = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
py = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

Px = np.zeros((h,w),np.uint8)
Py = np.zeros((h,w),np.uint8)

for i in range(1,h-1):
    for j in range(1,w-1):
        temp = (img[i-1][j-1]*px[0][0] + img[i-1][j]*px[0][1] + img[i-1][j+1]*px[0][2]+
                img[i][j-1]*px[1][0] + img[i][j]*px[1][1] + img[i][j+1]*px[1][2]+
                img[i+1][j-1]*px[2][0] + img[i+1][j]*px[2][1] +img[i+1][j+1]*px[2][2])
        Px[i][j] = temp

for i in range(1,h-1):
    for j in range(1,w-1):
        temp = (img[i-1][j-1]*py[0][0] + img[i-1][j]*py[0][1] + img[i-1][j+1]*py[0][2]+
                img[i][j-1]*py[1][0] + img[i][j]*py[1][1] + img[i][j+1]*py[1][2]+
                img[i+1][j-1]*py[2][0] + img[i+1][j]*py[2][1] +img[i+1][j+1]*py[2][2])
        Py[i][j] = temp

cv2.imshow('Horizontal Prewitt', Px)
cv2.waitKey()

cv2.imshow('Verticall Prewitt', Py)
cv2.waitKey()

P = Px + Py
cv2.imshow('Prewitt', P)
cv2.waitKey()

# sobel

sx = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sy = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

Sx = np.zeros((h,w),np.uint8)
Sy = np.zeros((h,w),np.uint8)

for i in range(1,h-1):
    for j in range(1,w-1):
        temp = (img[i-1][j-1]*sx[0][0] + img[i-1][j]*sx[0][1] + img[i-1][j+1]*sx[0][2]+
                img[i][j-1]*sx[1][0] + img[i][j]*sx[1][1] + img[i][j+1]*sx[1][2]+
                img[i+1][j-1]*sx[2][0] + img[i+1][j]*sx[2][1] + img[i+1][j+1]*sx[2][2])
        Sx[i][j] = temp

for i in range(1,h-1):
    for j in range(1,w-1):
        temp = (img[i-1][j-1]*sy[0][0] + img[i-1][j]*sy[0][1] + img[i-1][j+1]*sy[0][2]+
                img[i][j-1]*sy[1][0] + img[i][j]*sy[1][1] + img[i][j+1]*sy[1][2]+
                img[i+1][j-1]*sy[2][0] + img[i+1][j]*sy[2][1] +img[i+1][j+1]*sy[2][2])
        Sy[i][j] = temp

cv2.imshow('Horizontal Sobel', Sx)
cv2.waitKey()

cv2.imshow('Verticall Sobel', Sy)
cv2.waitKey()

S = Sx + Sy
cv2.imshow('Sobel', P)
cv2.waitKey()