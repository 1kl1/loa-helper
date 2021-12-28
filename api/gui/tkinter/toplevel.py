from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    root.geometry('200x200-100-100')
    root.resizable(True, True)
    root.overrideredirect(True)
    root.title("AppWindow Test")
    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', '1')

    l = Label(root, text="This is root window")
    l.pack()

    ttk.Button(root, text="Exit", command=root.destroy)
    button = ttk.Button(root, text='Exit', command=root.destroy)
    button.place(x=100, y=100)

    root.mainloop()


if __name__ == '__main__':
    main()
