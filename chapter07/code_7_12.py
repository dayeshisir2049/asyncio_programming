import tkinter
from time import sleep
from tkinter import ttk

windows = tkinter.Tk()
windows.title('Hello world app')
windows.geometry('200x100')


def say_hello():
    # sleep(5)
    print('Hello there')


hello_button = ttk.Button(windows, text='Say hello', command=say_hello)
hello_button.pack()

windows.mainloop()
