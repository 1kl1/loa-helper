import numpy as np
import cv2


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
