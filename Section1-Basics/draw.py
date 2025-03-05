import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') # Creating a blank image

# 1. Paint the image a certain color
# blank[200:300, 300:400] = 0, 255, 0 # Green
# cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (125, 125), (375, 375), (0, 255, 0), thickness=2) # Filled rectangle
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (250, 250), 125, (0, 0, 255), thickness=-1) # Filled circle
# cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (125, 125), (375, 375), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (125, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)