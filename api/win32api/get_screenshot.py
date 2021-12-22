import win32gui
import win32ui
import win32con
import win32api
import get_window


def saveScreenShot(x, y, width, height, path):
    # loa_window = get_window.find_loa_window()
    # loa_dc = win32gui.GetWindowDC(loa_window["hwnd"])
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

    # # save the bitmap to a file
    screenshot.SaveBitmapFile(mem_dc, path)
    # bits = screenshot.GetBitmapBits(True)
    # print(bits)
    # # free our objects
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

# 1250 65 1300 85


saveScreenShot(1250, 65, 50, 20, "test.bmp")
# f = open("test.bmp", 'rb')
# print(f.read())
