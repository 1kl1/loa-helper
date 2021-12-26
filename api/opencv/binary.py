import numpy as np
import cv2
from matplotlib import pyplot as plt


img = []
title = [
    "original",
    "otsu",
    "binary"
]
# image = cv2.imread('test.bmp')
original = cv2.imread('test_lined.bmp', cv2.IMREAD_GRAYSCALE)
img.append(original)
th1 = cv2.threshold(original, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
img.append(th1)
th2 = cv2.threshold(original, 120, 255, cv2.THRESH_BINARY)[1]
img.append(th2)

for i in range(3):
    plt.subplot(2, 2, i+1), plt.imshow(img[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()
