import time
import pyautogui
from time import sleep
import os


class autogui():
    def __init__(self, img, speed) -> None:
        self.img = img
        self.speed = speed
        pyautogui.FAILSAFE = True
    
    def nav_to_img(self):
        pos = pyautogui.locateOnScreen(self.img, confidence=.8)
        if pos is not None:
            pyautogui.moveTo(pyautogui.center(pos), duration=self.speed)
            pyautogui.click(pyautogui.center(pos))
            pyautogui.moveTo(0,2)
            return True
        print(pos)
        print(f"{self.img} is not found in the screen")
        return False

if __name__ == '__main__':
    path = os.path.join("image", "num4.png")
    autogui = autogui(path, speed=.1)
    i=0
    while True:
        if autogui.nav_to_img():
            print("working!")
        i+=1
        if i == 3:
            break
        