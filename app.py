import pyautogui
import time

pyautogui.FAILSAFE = False

for i in range(0,100):
    time.sleep(1)
    pyautogui.press('j')
    time.sleep(1)
    pyautogui.press('l')
    time.sleep(0.50)
    pyautogui.press('right')   
    time.sleep(0.30)
    pyautogui.press('right')   
    time.sleep(0.30)
    pyautogui.press('right')   
    time.sleep(0.30)
    pyautogui.press('enter')
