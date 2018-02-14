__author__ = '007'
__date__ = '2018/1/25'

from tkinter import *
import time
root = Tk()
root.title("text-test")
root.geometry("300x200")
root.resizable(width = True, height = False)
t = Text()
t.insert('1.0', 'text1\n')
t.insert(END, 'text2\n')
t.insert('1.0', 'text3\n')
t.delete('1.0', '2.0')
t.pack()

root.mainloop()