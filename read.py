# 读取图片，视频
import cv2 as cv

img = cv.imread('Photos/cat.jpg')

# img read
# cv.imshow('Cat', img)
# cv.imgshow('Cat', img)

# read Videos 读取一个视频小狗，如果小狗离开，则关闭视频
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()
