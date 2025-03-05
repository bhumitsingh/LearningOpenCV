import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\park.jpg')

# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # Translation matrix
    dimensions = (img.shape[1], img.shape[0]) # Width, Height
    return cv.warpAffine(img, transMat, dimensions) # Applying the translation matrix

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
# cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, center=None, scale=1.0):
    (height, width) = img.shape[:2] # Getting the height and width of the image

    if center is None: # If no center is given, use the middle of the image
        center = (width // 2, height // 2) # // for integer division

    # Perform the rotation
    M = cv.getRotationMatrix2D(center, angle, scale)
    rotated = cv.warpAffine(img, M, (width, height))

    return rotated

rotated = rotate(img, 90)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0) # 0 --> Vertical flip, 1 --> Horizontal flip, -1 --> Both
cv.imshow('Flip', flip)

cv.waitKey(0)