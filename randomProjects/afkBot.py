import pyautogui as pag
import random
import time

while True:
    x = random.randint(600,700)#generates a random x value between 600 and 700
    y = random.randint(200,700)#generates a random y value between 2000 and 700
    pag.moveTo(x,y,0.5)#0.5 is speed mouse will move to that coordinate
    time.sleep(100)#2 seconds
    