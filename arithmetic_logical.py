import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('image.jpg')

grey_img1 = cv2.imread('image.jpg',0)

cv2.imshow('img',img1)
cv2.waitKey()

cv2.imshow('img',grey_img1)
cv2.waitKey()

h,w = grey_img1.shape
cropped = grey_img1[int(h/2):,int(w/2):]
cv2.imshow('img',cropped)
cv2.waitKey()

img2 = cv2.imread('image2.jpeg')
cv2.imshow('img',img2)
cv2.waitKey()

grey_img2 = cv2.imread('image2.jpeg',0)
cv2.imshow('img',grey_img2)
cv2.waitKey()

resized_grey_img2 = cv2.resize(grey_img2,(w,h))
cv2.imshow('img',resized_grey_img2)
cv2.waitKey()

# Arithmetic operations

ar_add = cv2.add(grey_img1,resized_grey_img2)
cv2.imshow('ar_add',ar_add)
cv2.waitKey()

ar_sub = cv2.subtract(grey_img1,resized_grey_img2)
cv2.imshow('ar_sub',ar_sub)
cv2.waitKey()

# Logical operations

bitwise_and = cv2.bitwise_and(grey_img1,resized_grey_img2)
cv2.imshow('bitwise_and',bitwise_and)
cv2.waitKey()

plt.imshow(bitwise_and,cmap='gray')
plt.show()

bitwise_or = cv2.bitwise_or(grey_img1,resized_grey_img2)
cv2.imshow('bitwise_or',bitwise_or)
cv2.waitKey()

bitwise_xor = cv2.bitwise_xor(grey_img1,resized_grey_img2)
cv2.imshow('bitwise_xor',bitwise_xor)
cv2.waitKey()

bitwise_not = cv2.bitwise_not(grey_img1,resized_grey_img2)
cv2.imshow('bitwise_not',bitwise_not)
cv2.waitKey()