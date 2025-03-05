import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\cats.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canney = cv.Canny(blur, 125, 175)
# cv.imshow('Canney', canney)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # Parameters: Image, Threshold value, Max value, Threshold type
# THRESH_BINARY --> If pixel value is greater than the threshold value, it is assigned the max value, else 0
# THRESH_BINARY_INV --> If pixel value is greater than the threshold value, it is assigned 0, else the max value
# THRESH_TRUNC --> If pixel value is greater than the threshold value, it is assigned the threshold value, else the pixel value
# THRESH_TOZERO --> If pixel value is greater than the threshold value, it is assigned the pixel value, else 0
# THRESH_TOZERO_INV --> If pixel value is greater than the threshold value, it is assigned 0, else the pixel value
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) # Parameters: Image, Retrieval mode, Approximation method
# RETR_LIST --> Retrieves all the contours
# RETR_EXTERNAL --> Retrieves the external contours
# RETR_CCOMP --> Retrieves all the contours and creates a hierarchy
# RETR_TREE --> Retrieves all the contours and creates a full hierarchy
# CHAIN_APPROX_NONE --> Stores all the boundary points
# CHAIN_APPROX_SIMPLE --> Stores only the endpoints
# CHAIN_APPROX_TC89_L1 --> Applies Teh-Chin chain approximation algorithm
# CHAIN_APPROX_TC89_KCOS --> Applies Teh-Chin chain approximation algorithm

print(f'{len(hierarchies)} hierarchy level(s) found!')
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1) # Parameters: Image, Contours, Contour index (-1 means all contours), Color, Thickness
cv.imshow('Contours Drawn', blank)

cv.waitKey(0) # 0 means wait indefinitely for a key press