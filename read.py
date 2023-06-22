import cv2 as cv

img = cv.imread('Photos/cat.jpg')

# img read
# cv.imshow('Cat', img)
# cv.imgshow('Cat', img)

# read Videos
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read
    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()
