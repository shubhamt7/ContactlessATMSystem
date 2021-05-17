import cv2
import numpy as np
import time

from objectDetection import getInput
from colors import red, green, white, black, lowerMaskColor, upperMaskColor
from utility import Fade, CameraUtility

def keyboardHomepageLayout(frame, message, loggedIn, fontSize):

    x = 20
    y = 50
    cv2.rectangle(frame, (x, y), (x + 600, y + 120), black, 2)
    cv2.rectangle(frame, (x + 10, y + 10), (x + 590, y + 110), black, 2)
    cv2.putText(frame, message, (50, 120), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)


    x += 70
    cv2.rectangle(frame, (x, y + 200), (x + 200, y + 350), green, 2)
    cv2.rectangle(frame, (x + 250, y + 200), (x + 450, y + 350), red, 2)

    if(loggedIn == True):
        cv2.putText(frame, "CONTINUE", (100, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.2, green, 2)
        cv2.putText(frame, "LOG OUT", (360, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.2, red, 2)
    else:
        cv2.putText(frame, "LOG IN", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.4, green, 2)
        cv2.putText(frame, "EXIT", (390, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.4, red, 2)


def determineKey(cx, cy):
    if cy > 250 and cy < 400:
        if cx > 90 and cx < 290:

            return "enter"
        elif cx > 340 and cx < 540:
            return "exit"
        else:
            return ""
    else:
        return ""


def getHomepageKey(message="", loggedIn = False, fontSize = 1.2):

    result = getInput(determineKey, keyboardHomepageLayout, "homepage", (message, loggedIn, fontSize))
    return result


