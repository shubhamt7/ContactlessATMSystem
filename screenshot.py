"""
This file contains code responsible for clicking
the screenshot of the user once he logs in
"""

import os
import pyautogui
import time
from datetime import date
import cv2
import numpy as np
import os.path as path
from pathlib import Path

#Function for getting current date and time
def getCurrentDateAndTime():
    t = time.localtime()
    currentTime = time.strftime("%H_%M_%S", t)
    currentDate = date.today().strftime("%d_%m_%y")
    return currentDate, currentTime


#Clicking screenshot of the user and storing it in images directory
def clickScreenshot(ac=""):

    #Computing the directory name based on current date
    currentDate, currentTime = getCurrentDateAndTime()
    current_dir = Path.cwd()
    destination_dir = path.join(current_dir, "images", str(currentDate))

    if not path.exists(destination_dir):
        os.mkdir(destination_dir)

    # Computing the image file name based on current time and user account number
    fileName = ac + "_time-" + str(currentTime) + '.png'
    filePath = path.join(destination_dir, fileName)


    #Clicking the screenshot and writing it to the computed file path
    windowRect = cv2.getWindowImageRect('Contactless ATM System')
    x = windowRect[0]
    y = windowRect[1]
    w = windowRect[2]
    h = windowRect[3]
    image = pyautogui.screenshot(region=(x, y, w, h - 120))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(filePath, image)
