import cv2
import win32gui
import win32ui
import win32con
import numpy as np


def saveScreenShot(x, y, width, height, path):
    loa_dc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
    img_dc = win32ui.CreateDCFromHandle(loa_dc)

    # # create a memory based device context
    mem_dc = img_dc.CreateCompatibleDC()

    # # create a bitmap object
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    # # copy the screen into our memory device context
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (x, y), win32con.SRCCOPY)

    bits = screenshot.GetBitmapBits(False)
    bits = np.asanyarray(bits, dtype=np.uint8)
    bits = np.reshape(bits, (width, -1))

    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())
    return bits

# 1250 65 1300 85


# bits = saveScreenShot(100, 100, 500, 200, "test.bmp")
# print(bits)
# frame = cv2.imdecode(bits, cv2.IMREAD_COLOR)
# print(frame)
# frame.imshow()

file = open("test_lined.bmp", "rb")
frame = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
# 미완
