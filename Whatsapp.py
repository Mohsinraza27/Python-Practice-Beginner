import pyautogui as gui

import time

message = input("Enter your Message...")
limit = input('Enter your limit...')

time.sleep(2)

for i in range(int(limit)):
    gui.typewrite(message)
    gui.press('Enter')

