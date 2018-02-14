__author__ = '007'
__date__ = '2018/1/25'

from tkinter import *
root = Tk()
root.title("frame-test")
root.geometry("200x300")
root.resizable(width = True, height = False)
Label(root, text = 'frame', bg = 'red', font = ('Arial',15)).pack()
frm = Frame(root)
frm_L = Frame(frm)
Label(frm_L, text = '左上', bg = 'pink', font = ('Arial',12)).pack(side = TOP)
Label(frm_L, text = '左下', bg = 'green', font = ('Arial',12)).pack(side = TOP)
frm_L.pack(side = LEFT)
frm_R = Frame(frm)
Label(frm_R, text = '右上', bg = 'yellow', font = ('Arial',12)).pack(side = TOP)
Label(frm_R, text = '右下', bg = 'purple', font = ('Arial',12)).pack(side = TOP)
frm_R.pack(side = RIGHT)
frm.pack()
root.mainloop()