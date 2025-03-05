import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\cats2.jpg')
cv.imshow('Cats2', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Masked Gray', mask)

# Gray Histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256]) 
# Parameters: Image, Channel, Mask, Histogram size, Range
# Range is the range of the values in the image
# Histogram size is the number of bins in the histogram
# Mask is the mask applied to the image
# Channel is the channel of the image
# Image is the image to be processed

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.show()

cv.waitKey(0)