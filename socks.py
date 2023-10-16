"""
Welcome to florr.io auto working engine!
"""
import os
import re
import pyautogui as gui
from time import sleep
from PIL import Image
import aircv as ac

def screen():
    img = gui.screenshot()
    img.save("screenshot.png")
    imsrc = ac.imread("screenshot.png")
    imsch1 = ac.imread("img/query.jpg")
    imsch2 = ac.imread("img/check.jpg")
    global match_result1, match_result2
    match_result1 = ac.find_all_template(imsrc, imsch1, 0.85)
    points1=[]
    points2=[]
    for i in match_result1:
        points1.append((i['result']))
    points1e = eval(str(points1).replace('(', '').replace(')', ''))
    print(points1e)
    while True:
        gui.click(x = points1e[0]/2, y = points1e[1]/2, duration = 0)
        match_result2 = ac.find_all_template(imsrc, imsch2, 0.85)
        for i in match_result2:
            points2.append((i['result']))
        if points2 != []:
            points2e = eval(str(points2).replace('(', '').replace(')', ''))
            print(points2e)
            gui.click(x = points2e[0]/2, y = points2e[1]/2, duration = 0)
            os.system('say 快来抢票呀')
            while True:
                sleep(1)
if __name__ == "__main__":
    screen()
