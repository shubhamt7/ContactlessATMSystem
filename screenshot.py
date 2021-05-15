import pyautogui
import time
from datetime import date
import cv2
import numpy as np

def getCurrentDateAndTime():
    t = time.localtime()
    currentTime = time.strftime("%H_%M_%S", t)
    currentDate = date.today().strftime("%d_%m_%y")

    return currentDate, currentTime

def clickScreenshot(name = "", ac = ""):

    currentTime, currentDate = getCurrentDateAndTime()
    destination_dir = "/home/shubham/PycharmProjects/ContactlessATMSystem/images/"

    name = name.lower()
    name = name.replace(" ", "")

    fileName = name + "_" + ac + "_date-" + str(currentDate) + "_time-" + str(currentTime) + '.png'
    filePath = destination_dir + fileName
    image = pyautogui.screenshot(region=(60, 20, 650, 490))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(filePath, image)


# clickScreenshot("Shubham Thind")

