#mbc.pyw - save and loads pieces of text to the clipboard.
#Usage: python mcb.py save <keyword> - Save clipboard to keyword
#       python mcb.py <keyword> - loads keyword to clipbord.
#       python mcb.py list - load all keyword to clipboard
#		python mcb.py del <keyword>
import shelve, pyperclip,sys

mcbShelf  = shelve.open("mbc")

if len(sys.argv) == 3 :
	if sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower == "del":
    	if sys.argv[2] in  mcbShelf:
    		del mcbShelf[sys.argv[2]]
    	else:
    		print("没有这个关键字.")
    else:
    	print("语法错误。")
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in  mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print("没有这个关键字对应的复制内容")
else:
    print("错误语法！")
mcbShelf.close()