import cv2 as cv

img = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

# Averaging - Averaging is done by convolving the image with a normalized box filter. 
#             It simply takes the average of all the pixels under the kernel area and 
#             then replaces the central element

average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

# Gaussian Blur - Gaussian blurring is highly effective in removing Gaussian noise from 
#                 the image. It actually uses the Gaussian distribution for calculating
#                 the pixel value. It is done using the GaussianFilter() method.

gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gaussian)

# Median Blur - Median blurring is highly effective in removing salt-and-pepper noise.
#               It replaces each pixel's value with the median of its neighboring pixels.
#               It is done using the medianBlur() method.

median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral Blur - Bilateral blurring is highly effective in noise removal while keeping
#                  the edges sharp. It is done using the bilateralFilter() method.

bilateral = cv.bilateralFilter(img, 9, 75, 75)
# Parameters: Image, 
#             Diameter of the pixel neighborhood : It is the number of pixels away from the current pixel being considered.
#             Sigma color : A larger value of sigma color means that more colors will be considered within the pixel neighborhood.
#             Sigma space : A larger value of sigma space means that pixels farther out from the central pixel will influence the blurring calculation.
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0) # 0 means wait indefinitely for a key press
cv.destroyAllWindows() # Destroy all windows