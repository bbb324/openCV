# 画颜色的方块
import cv2 as cv
import numpy as np

# 3 代表【红，蓝，绿】三色通道
blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('blank', blank)

# 画方块

# blank[:] = 0,25,2 # 填充颜色，只能用16进制数字，不能用 white, #FFFFFF 这样的
#blank[200:300, 300:400] = 0,255,0 # 在w:300, h:400的位置展示一个 w200,h300的图片
#cv.imshow('white', blank)

# thickness=-1 表示全涂满
# 从 (0,0) 到 (500,255) 的位置画一个颜色为 0,255,0 的框（blank = npmzeros），边框值为2
#cv.rectangle(blank, (0,0), (500,255), (0,255,0), thickness=10)
#cv.imshow('rectangle', blank)



# 画圆圈
# 40 代表半径
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
# cv.imshow('circle', blank)
# cv.waitKey(0)

# 画线
# cv.line(blank, (0,0), (255, 255), (0,255,255), thickness=3)
# cv.imshow('line', blank)
# cv.waitKey(0)

# 写文字 (0,255) 是位置， 3.0 是font-size
cv.putText(blank, 'Hello', (0,255), cv.FONT_HERSHEY_TRIPLEX, 3.0, (0,255,0),thickness=1)
cv.imshow('text', blank)
cv.waitKey(0)