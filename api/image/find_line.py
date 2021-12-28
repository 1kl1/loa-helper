import numpy as np
import cv2
# from matplotlib import pyplot as plt

src = cv2.imread('test.bmp', cv2.IMREAD_GRAYSCALE)
# dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)[1]

# print(dst.shape)

# img = []
# title = ["top", "mid", "bot"]


# img.append(dst[0:4, :])
# # img.append(dst[4:16:, :])
# img.append(dst[16:20, :])

# for i in range(2):
#     plt.subplot(2, 2, i+1), plt.imshow(img[i], 'gray')
#     plt.title(title[i])
#     plt.xticks([]), plt.yticks([])

# plt.show()


def isEmptyImage(src):
    for i in src:
        for j in i:
            if j == 255:
                return False
    return True


def isHaveLine(src):  # src must be grayscale
    dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY)[1]
    if isEmptyImage(dst[0:4, :]) and isEmptyImage(dst[16:20, :]):
        return False
    else:
        return True


print(isHaveLine(src))
