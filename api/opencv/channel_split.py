import numpy as np
import cv2

src = cv2.imread("image/test_lined.bmp", cv2.IMREAD_COLOR)
b = src[:, :, 0]
g = src[:, :, 1]
r = src[:, :, 2]
# [h,w,c]

height, width, channel = src.shape
zero = np.zeros((height, width, 1), dtype=np.uint8)
bgz = cv2.merge((b, g, zero))
# 빈 이미지
