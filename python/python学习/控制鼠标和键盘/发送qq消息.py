#必需以管理员身份运行

import pyautogui, time, pyperclip

#启动下方窗口(609, 767)
pyautogui.moveTo((609, 767))

#qq位置坐标(1155, 745)
time.sleep(1)#软件反应较慢
pyautogui.click((1155, 745))

#文字输入区位置(1108, 141)
time.sleep(1)
pyautogui.click((1108, 141))

#输入汉字区
time.sleep(1)
#qq第一次输入会阻止pyautogui.typewrite("刘为齐")只是不阻止特殊键
#清空输入框
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("backspace")
#输入汉字
pyperclip.copy("刘为齐")
pyautogui.hotkey("ctrl", "v")

#点击进入对话匡
#人物位置(1153, 189)
time.sleep(3)
pyautogui.doubleClick((1153, 200))
#pyautogui.typewrite("enter")

#进入对话框输入
time.sleep(1)
#qq 阻止pyautogui.typewrite("刘为齐，你什么时候来这边？")
#(482, 583)
pyperclip.copy("刘为齐，你什么时候来这边？")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

