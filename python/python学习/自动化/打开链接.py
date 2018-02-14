import  webbrowser, sys, pyperclip
#获得地址
if len(sys.argv) > 1:
    adress = " ".join(sys.argv[1 :])
else:
    adress = pyperclip.paste()

webbrowser.open(adress)