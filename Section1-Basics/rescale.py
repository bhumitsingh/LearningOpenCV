import cv2 as cv

# img = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\cat_large.jpg')
# cv.imshow('Cat', img) # Displaying the image

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Videos\dog.mp4')

while True:
    isTrue, frame = capture.read() # Read the video frame by frame

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame) # Display the frame
    cv.imshow('Video Resized', frame_resized) # Display the

    if cv.waitKey(20) & 0xFF==ord('d'): # If 'd' key is pressed, break the loop
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0) # 0 means wait indefinitely for a key press