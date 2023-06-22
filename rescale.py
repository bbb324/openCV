# resize 一个视频，或者图片
import cv2 as cv


# 图片、视频，直播摄像头尺寸压缩处理
def rescaleFrame(frame, scale=0.15):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    # 定义压缩宽窄
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # live video only 仅能用于直播
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resize = rescaleFrame(frame, scale=.2)
    cv.imshow('Video Resized', frame_resize)

    # 如果狗狗离开，则关闭视窗
    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()