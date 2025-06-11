import pyautogui
import time
import keyboard


Cx = 717
Cy = 365

Ux1 = 544
Ux2 = 644
Ux3 = 744

Uy = 560
time.sleep(1)

keyboard.press_and_release('alt+tab')

time.sleep(1)


try:
    while True:
        for i in range(100):
            pyautogui.moveTo(Cx, Cy)  
            pyautogui.click()
            

        for i in range(10):
            pyautogui.moveTo(Ux1, Uy)
            pyautogui.click()
              

        for i in range(10):
            pyautogui.moveTo(Ux2, Uy)
            pyautogui.click()
             

        for i in range(10):
            pyautogui.moveTo(Ux3, Uy)
            pyautogui.click()
             

except:
    keyboard.wait('esc')