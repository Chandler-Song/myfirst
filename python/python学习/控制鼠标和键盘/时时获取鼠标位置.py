# Displays the mouse cursor's current position.
import pyautogui
print("Press Ctrl+C to quit.")
#TODO: Get and print the mouse coordinates.
try:
    while True:
        Str = "X:" + str(pyautogui.position()[0]).rjust(4) + " Y:" + str(pyautogui.position()[1]).rjust(4)
        print(Str, end = '')
        print("\b" * len(Str), end = '', flush = True)
except :
    print("\n done.")
