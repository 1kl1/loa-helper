import tkinter as tk
from tkinter import ttk
import datetime
from PIL import Image, ImageTk


def main():
    root = tk.Tk()
    root.geometry('200x200-100-100')
    root.overrideredirect(True)
    root.title("Realtime Window")
    # root.wm_attributes("-disabled", True)
    root.wm_attributes("-alpha", "0.8")
    root.wm_attributes("-topmost", True)

    ttk.Button(root, text="Exit", command=root.destroy)
    button = ttk.Button(root, text='Exit', command=root.destroy)
    button.place(x=185, y=195, anchor="se")
    label = tk.Label(root, text="placeholder")
    label.pack()

    img = Image.open('test.bmp')
    img = ImageTk.PhotoImage(img)

    img_label = tk.Label(root, image=img)
    img_label.pack()

    def set_label():
        currTime = datetime.datetime.now()
        label['text'] = currTime
        # _img = Image.open('test.bmp')
        # _tkImg = ImageTk.PhotoImage(_img)
        img_label['image'] = img
        root.after(1000, set_label)

    set_label()
    root.mainloop()


if __name__ == '__main__':
    main()
