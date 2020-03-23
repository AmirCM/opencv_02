import numpy as np
import cv2 as cv

img = cv.imread('python.png')
cv.namedWindow('img', cv.WINDOW_AUTOSIZE)

px = img.item(150, 200, 2)
print(px, img[150, 200])

img.itemset((150, 200, 2), 0)
img[150, 200, 2] = px

print(f'shape => {img.shape}')
print(f'size => {img.size}')
print(f'value type => {img.dtype}')

roi = img[100:300, 100:300]

b, g, r = cv.split(img)
img = cv.merge((b, g, r))
b = img[:, :, 0]

cv.imshow('img', img)
cv.imshow('roi', roi)
cv.waitKey(0)
