import cv2 as cv

# img = cv.imread(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Photos\cat_large.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

# Reading Videos

capture = cv.VideoCapture(r'C:\Users\bhumi\Documents\LearningOpenCV\Resources\Videos\dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()