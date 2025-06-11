import pyautogui as py
import time
import keyboard

print("Press 'q' to stop.")

while True:
    print(py.position())
    time.sleep(1)
    
    if keyboard.is_pressed('q'):
        print("Stopping the script...")
        break
