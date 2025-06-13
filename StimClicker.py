import pyautogui
import time
import keyboard


Cx = 717
Cy = 365

Ux1 = 544
Ux2 = 644
Ux3 = 744

Uy = 560

Sx = 675
Sy = 695
Sy2 = 770

Ly = 230

time.sleep(1)

keyboard.press_and_release('alt+tab')

time.sleep(1)



while True:

    print("Stimulating...")
    pyautogui.moveTo(Cx, Cy)    
    for i in range(100):  
        pyautogui.click()
        
    print("Upgrading...")
    pyautogui.moveTo(Ux1, Uy)
    for i in range(10):
        pyautogui.click()
              
    print("Upgrading...")
    pyautogui.moveTo(Ux2, Uy)
    for i in range(10):
        pyautogui.click()
             
    print("Upgrading...")
    pyautogui.moveTo(Ux3, Uy)
    for i in range(10):
        pyautogui.click()

    print("Squishing...")
    for i in range(3):
        pyautogui.moveTo(Sx, Sy)
        pyautogui.click()
        pyautogui.moveTo(Sx, Sy2)
        pyautogui.click()
             
    pyautogui.moveTo(Ux3, Ly)
    pyautogui.click()

