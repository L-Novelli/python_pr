import pyautogui
import time

time.sleep(7)

f = open("jajaxd", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
