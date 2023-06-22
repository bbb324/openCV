import cv2 as cv
img = cv.imread('Photos/park.jpg')
#cv.imshow('normal', img)
# 灰度一个图片
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)


# 图片模糊处理
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)




# edge cascade 图片边界监测
# 可以通过blur 进行模糊化处理，来减轻画边界时内容过多
# canny = cv.Canny(img, 125, 175) # 对比起来边界信息过多
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('canny', canny)

# dilated the img 膨胀？？ 不知道干啥用的，跟canny 差不多
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('dialated', dilated)


#eroded 图片
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('eroded', eroded)


# resize 图片 interpolation是图片质量处理如果是图片放大  cv.cv.INTER_CUBIC 质量会高一些
# resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resize', resize)


# cropping 图片裁剪
cropped = img[50:200, 200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)