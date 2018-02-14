__author__ = '007'
__date__ = '2018/1/25'

from tkinter import *
root = Tk()
root.title("scrl-test")
root.geometry()
def print_item(event):
	print( lb.get(lb.curselection()))
var = StringVar()
lb = Listbox(root, listvariable = var, height = 5, selectmode = BROWSE)
lb.bind('<ButtonRelease-1>',print_item)
list_item = [1,2,3,4,5,6,7,8,9,0]
for item in list_item:
	lb.insert(END, item)
scrl = Scrollbar(root)
scrl.pack(side = RIGHT, fill = Y)
lb.configure(yscrollcommand = scrl.set) #指定Listbox的yscrollbar的回调函数为Scrollbar的set，表示滚动条在窗口变化时实时更新
lb.pack(side = LEFT, fill = BOTH)
scrl['command'] = lb.yview
root.mainloop()