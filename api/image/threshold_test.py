import numpy as np
import cv2
from matplotlib import pyplot as plt


img = []
title = [
    "original",
    "global",
    "adaptive mean",
    "adaptive gaussian"
]
# image = cv2.imread('test.bmp')
original = cv2.imread('test.bmp', cv2.IMREAD_GRAYSCALE)
img.append(original)
ret, th1 = cv2.threshold(
    original, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
img.append(th1)
img.append(cv2.adaptiveThreshold(original, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 11, 2))
img.append(cv2.adaptiveThreshold(original, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 11, 2))


for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(img[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()
