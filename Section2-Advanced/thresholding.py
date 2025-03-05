import cv2 as cv

img = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding : Thresholding is used to binarize the image (0 or 1) based on the threshold value
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholding Inverse', thresh_inv)

# Adaptive Thresholding : Thresholding is used to binarize the image (0 or 1) based on the threshold value
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1) # Parameters: Image, Max value, Adaptive method, Threshold type, Block size, Constant
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)