__author__ = '007'
__date__ = '2018/1/25'

from tkinter import *
import time
root = Tk()
root.title("entry-test")
root.geometry("300x200")
root.resizable(width = True, height = False)
var = StringVar()
e = Entry(root, textvariable = var)
var.set("entry")
print(var.get())
time.sleep(3)
var.set("刘必勇")
print(var.get())
e.pack()
root.mainloop()