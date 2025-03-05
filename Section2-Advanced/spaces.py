import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\park.jpg')
cv.imshow('park', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale (Gray)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV (Hue, Saturation, Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b (L stands for lightness) (a and b for the color spectrums)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('L*a*b', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

# L*a*b to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('L*a*b to BGR', lab_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)