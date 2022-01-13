import tkinter as tk
from tkinter import ttk
import datetime
from PIL import Image, ImageTk
from get_screenshot import saveScreenShot
from find_line import isHaveLine
import cv2


def main():
    root = tk.Tk()
    root.geometry('200x200-100-100')
    root.overrideredirect(True)
    root.title("Realtime Window")
    # root.wm_attributes("-disabled", True)
    root.wm_attributes("-alpha", "0.5")
    root.wm_attributes("-topmost", True)

    button = ttk.Button(root, text='Exit', command=root.destroy)
    button.place(x=185, y=195, anchor="se")
    lined_label = tk.Label(root, text="placeholder")
    lined_label.pack()

    saveScreenShot(1250, 65, 50, 20, "test.bmp")
    img = Image.open('test.bmp')
    img = ImageTk.PhotoImage(img)

    img_label = tk.Label(root, image=img)
    img_label.pack()

    x_ = tk.StringVar(value="1135")
    y_ = tk.StringVar(value="50")
    w_ = tk.StringVar(value="50")
    h_ = tk.StringVar(value="20")
    textBox1 = ttk.Entry(root, width=10, textvariable=x_)
    textBox2 = ttk.Entry(root, width=10, textvariable=y_)
    textBox3 = ttk.Entry(root, width=10, textvariable=w_)
    textBox4 = ttk.Entry(root, width=10, textvariable=h_)
    textBox1.pack()
    textBox2.pack()
    textBox3.pack()
    textBox4.pack()

    def set_label():
        src = cv2.imread('tmp/test.bmp', cv2.IMREAD_GRAYSCALE)
        isLineText = "Lined" if isHaveLine(src) else "NoLined"
        print(isLineText)
        lined_label.configure(text=isLineText)
        lined_label.text = isLineText
        saveScreenShot(int(x_.get()), int(y_.get()), int(
            w_.get()), int(h_.get()), "test.bmp")
        new = ImageTk.PhotoImage(Image.open('test.bmp'))
        img_label.configure(image=new)
        img_label.image = new
        root.after(100, set_label)

    set_label()
    root.mainloop()


if __name__ == '__main__':
    main()
