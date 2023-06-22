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

# 从 (0,0) 到 (500,255) 的位置画一个颜色为 0,255,0 的框（blank = npmzeros），边框值为2
cv.rectangle(blank, (0,0), (500,255), (0,255,0), thickness=10)
cv.imshow('rectangle', blank)
cv.waitKey(0)