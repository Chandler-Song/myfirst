import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
pyautogui.size()
for i in range(10):
    pyautogui.moveTo(100, 100, duration = 0.25)
    pyautogui.moveTo(200, 100, duration = 0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
for i in range(10):
    pyautogui.moveRel(100, 0, duration = 0.25)
    pyautogui.moveRel(0, 100, duration = 0.25)
    pyautogui.moveRel(-100, 0, duration = 0.25)
    pyautogui.moveRel(0, -100, duration = 0.25)
pyautogui.position()
#


import pyautogui
#点击鼠标
pyautogui.click()
pyautogui.click(10, 5)
pyautogui.click(10, 5, button = "left")
pyautogui.click(10, 5, button = "right")
pyautogui.mouseDown()
pyautogui.mouseUp()
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
#拖动鼠标
pyautogui.dragTo()
pyautogui.dragRel()
#滚动鼠标
pyautogui.scroll(200)
#处理屏幕
im = pyautogui.screenshot()
im.getpixel((0, 0))
im.getpixel((50, 100))
pyautogui.pixelMatchesColor(50, 200, (135, 136, 144))
#图像识别
pyautogui.locateOnScreen("submit.png")
pyautogui.center((643,745,70, 29))
pyautogui.doubleclick(pyautogui.center(pyautogui.locateOnScreen("submit.png")))
#控制键盘
pyautogui.typewrite("Hello world!")
pyautogui.typewrite(['a', 'b', 'left', 'X', 'Y'])
pyautogui.KeyDown()
pyautogui.KeyUp()
pyautogui.press()
#热键组合
pyautogui.hetkey("ctrl", "c")