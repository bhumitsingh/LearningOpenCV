import cv2 as cv
import numpy as np

# ----Masking A Circle----

img1 = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\park.jpg')
cv.imshow('Park1', img1)

blank1 = np.zeros(img1.shape[:2], dtype='uint8')
cv.imshow('Blank1', blank1)

# Mask (Circle)
mask_circle = cv.circle(blank1, (img1.shape[1]//2, img1.shape[0]//2), 100, 255, -1)
# Parameters: Image, Center, Radius, Color, Thickness
cv.imshow('Mask_Circle', mask_circle)

# Masked Image (Circle)
masked_circle = cv.bitwise_and(img1, img1, mask=mask_circle)
# Parameters: Source, Destination, Mask
cv.imshow('Circle Mask Applied to Image', masked_circle)

# Masking A Rectangle

img2 = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\park.jpg')
cv.imshow('Park2', img2)

blank2 = np.zeros(img2.shape[:2], dtype='uint8')
cv.imshow('Blank2', blank2)

# ----Mask (Rectangle)----
mask_rectangle = cv.rectangle(blank2,(300,0), (600,400), 255, -1) 
# Parameters: Image, Start Point, End Point, Color, Thickness
cv.imshow('Mask_Rectangle', mask_rectangle)

# Masked Image (Rectangle)
masked_rectangle = cv.bitwise_and(img2, img2, mask=mask_rectangle)
# Parameters: Source, Destination, Mask 
cv.imshow('Rectangle Mask Applied to Image', masked_rectangle)

# ----Combined Mask----
combined_mask = cv.bitwise_and(mask_circle, mask_rectangle)
cv.imshow('Combined Mask', combined_mask)

# Masked Image (Combined)
masked_combined = cv.bitwise_and(img2, img2, mask=combined_mask)
cv.imshow('Combined Mask Applied to Image', masked_combined)

cv.waitKey(0)