import win32con
import win32gui
import json


# get_windows() -> array(window: dict)
# window {hwnd:, visible:, title:, minimized:, maximized:, rectangle:tuple(left, top, right, bottom)}

# 현재 컴퓨터에서 실행중인 모든 프로세스의 윈도우를 리턴하는 함수
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


if __name__ == "__main__":
    loa_window = find_loa_window()
    if loa_window:
        print(json.dumps(loa_window))
    else:
        raise(Exception("Cannot Find Lostark Process."))

# 2021.12.21 오후 10시자 로스트아크 프로제스명은 아래와 같다.
#"LOST ARK (64-bit) v.2.20.2.1"
