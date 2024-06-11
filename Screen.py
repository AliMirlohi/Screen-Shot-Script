import pyautogui
import time
from random import randint

class scr():
    def photo():
        while True:
            x=randint(0,100000)
            pic=pyautogui.screenshot()
            pic.save(f'C:/.../{x}.jpg')  # ... -> your address
            time.sleep(4)


scr.photo()
