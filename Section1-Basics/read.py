import cv2 as cv

img = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\cat_large.jpg')

cv.imshow('Cat', img) # Displaying the image

cv.waitKey(0) # 0 means wait indefinitely for a key press
cv.destroyAllWindows() # Destroy all windows

# Reading Videos

capture = cv.VideoCapture(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Videos\dog.mp4')

while True:
    isTrue, frame = capture.read() # Read the video frame by frame
    cv.imshow('Video', frame) # Display the frame

    if cv.waitKey(20) & 0xFF==ord('d'): # If 'd' key is pressed, break the loop
        break

capture.release()
cv.destroyAllWindows()