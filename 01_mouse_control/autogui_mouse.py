import pyautogui
import time

def draw_letter(letter:str):
    """draw a letter based on the input argument"""
    sec=3
    start_pos=(500, 500)
    if letter.upper() == "H":
        pyautogui.moveTo(start_pos)
        pyautogui.move(0, 200,duration=sec)
        pyautogui.move(0, -100, duration=sec/2)
        pyautogui.move(200, 0, duration=sec/2)
        pyautogui.move(0, -100, duration=sec/2)
        pyautogui.move(0, 200, duration=sec)
        return True
    else:
        return False

pyautogui.FAILSAFE = False

while True:
    ip="hello world!"
    for i in range(len(ip)):
        print(ip[i])
        draw_letter(ip[i])
    break
