import win32gui
import win32ui
import win32con


def saveScreenShot(x, y, width, height, path):
    loa_window = find_loa_window()
    loa_dc = win32gui.GetWindowDC(loa_window["hwnd"])
    # loa_dc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
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


def get_windows():
    def sort_windows(windows):
        sorted_windows = []
        # Find the first entry
        for window in windows:
            if window["hwnd_above"] == 0:
                sorted_windows.append(window)
                break
        else:
            raise(IndexError("Could not find first entry"))

        # Follow the trail
        while True:
            for window in windows:
                if sorted_windows[-1]["hwnd"] == window["hwnd_above"]:
                    sorted_windows.append(window)
                    break
            else:
                break

        # Remove hwnd_above
        for window in windows:
            del(window["hwnd_above"])

        return sorted_windows

    def enum_handler(hwnd, results):
        window_placement = win32gui.GetWindowPlacement(hwnd)

        results.append({
            "hwnd": hwnd,
            "visible": win32gui.IsWindowVisible(hwnd) == 1,
            # Window handle to above window
            "hwnd_above": win32gui.GetWindow(hwnd, win32con.GW_HWNDPREV),
            "title": win32gui.GetWindowText(hwnd),
            "minimized": window_placement[1] == win32con.SW_SHOWMINIMIZED,
            "maximized": window_placement[1] == win32con.SW_SHOWMAXIMIZED,
            # (left, top, right, bottom)
            "rectangle": win32gui.GetWindowRect(hwnd)
        })

    enumerated_windows = []
    win32gui.EnumWindows(enum_handler, enumerated_windows)
    return sort_windows(enumerated_windows)

# 로아가 실행중이라면 window 개체를, 아니라면 none을 리턴한다.


def find_loa_window():
    windows = get_windows()
    candidateWindows = []

    for window in windows:
        if window["title"] != "" and window["visible"]:
            candidateWindows.append(window)

    for window in candidateWindows:
        if window["title"].startswith("LOST ARK"):
            return window

    print("Cannot find process!!")
    return None
