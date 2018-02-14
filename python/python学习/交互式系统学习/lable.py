__author__ = '007'
__date__ = '2018/1/25'

from tkinter import *
root = Tk()
root.title("label-test")
root.geometry("200x300")
root.resizable(width = True, height = False)
l = Label(root, text = 'lable', bg = 'pink', font = ('Arial',12), width = 8, height = 3)
l.pack(side = RIGHT)
root.mainloop()