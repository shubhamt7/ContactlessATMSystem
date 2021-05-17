import os

import pyautogui
import time
from datetime import date
import cv2
import numpy as np
import os.path as path
from pathlib import Path

def getCurrentDateAndTime():
    t = time.localtime()
    currentTime = time.strftime("%H_%M_%S", t)
    currentDate = date.today().strftime("%d_%m_%y")

    return currentDate, currentTime

def clickScreenshot(ac = ""):

    currentDate, currentTime = getCurrentDateAndTime()

    current_dir = Path.cwd()
    destination_dir = path.join(current_dir, "images", str(currentDate))

    if(path.exists(destination_dir) == False):
        os.mkdir(destination_dir)

    fileName = ac + "_time-" + str(currentTime) + '.png'
    filePath = path.join(destination_dir, fileName)
    windowRect = cv2.getWindowImageRect('Contactless ATM System')
    x = windowRect[0]
    y = windowRect[1]
    w = windowRect[2]
    h = windowRect[3]
    image = pyautogui.screenshot(region=(x,y,w,h))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(filePath, image)


