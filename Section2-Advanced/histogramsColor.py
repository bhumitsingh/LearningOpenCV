import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\cats2.jpg')
cv.imshow('Cats2', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Color', masked)

# Color Histogram
colors = ('b', 'g', 'r') # Blue, Green, Red
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)