import win32gui
import time


while True:
    pos = win32gui.GetCursorPos()
    print(pos)
    time.sleep(0.00001)
