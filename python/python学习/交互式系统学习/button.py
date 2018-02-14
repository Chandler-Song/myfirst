__author__ = '007'
__date__ = '2018/1/25'

from tkinter import *
root = Tk()
root.title("button-test")
root.geometry("500x500")
def printhello():
	t.insert(END, 'hello\n')
t = Text()
t.pack()
Button(root, text = 'press', command = printhello).pack()#默认位置在200，400
root.mainloop()