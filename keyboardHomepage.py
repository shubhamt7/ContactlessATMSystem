import cv2
import numpy as np
import time

from objectDetection import getInput
from colors import red, green, white, black, blue, lowerMaskColor, upperMaskColor
from utility import Fade, CameraUtility, getHindiMessage

def keyboardHomepageLayout(frame, language, message, loggedIn, fontSize):

    x = 20
    y = 50
    cv2.rectangle(frame, (x, y), (x + 600, y + 120), black, 2)
    cv2.rectangle(frame, (x + 10, y + 10), (x + 590, y + 110), black, 2)

    x += 70
    cv2.rectangle(frame, (x, y + 200), (x + 200, y + 350), green, 2)
    cv2.rectangle(frame, (x + 250, y + 200), (x + 450, y + 350), red, 2)

    fontSize = 0.8
    #deciding message to be displayed
    messageColor = white
    if(language == "english"):
        if(message == "transfer-success"):
            message = "Money transferred successfully!"
        elif(message == "withdraw-success"):
            message = "Money withdrawn successfully"
        elif(message == "cancelled-txn"):
            message = "Transaction cancelled succesfully"
        elif(message == "welcome-message"):
            message = "Welcome to Contactless ATM!"
            fontSize = 1
        else:
            pass
    elif(language == "hindi"):
        if (message == "transfer-success"):
            message = "पैसा सफलतापूर्वक ट्रांसफर किया गया"
        elif (message == "withdraw-success"):
            message = "पैसा सफलतापूर्वक निकाला गया"
        elif (message == "cancelled-txn"):
            message = "सफलतापूर्वक रद्द किया गया"
        elif(message == "welcome-message"):
            message = "CATM में आपका स्वागत है!"
        else:
            pass
    else:
        pass

    if(language == "english"):
        cv2.putText(frame, message, (50, 120), cv2.FONT_HERSHEY_SIMPLEX, fontSize, messageColor, 2)
        if (loggedIn == True):
            cv2.putText(frame, "CONTINUE", (100, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.2, green, 2)
            cv2.putText(frame, "LOG OUT", (360, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.2, red, 2)
        else:
            cv2.putText(frame, "LOG IN", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.4, green, 2)
            cv2.putText(frame, "EXIT", (390, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.4, red, 2)
    elif(language == "hindi"):
        frame = getHindiMessage(msg=message, frame=frame, x=50, y=90, color=messageColor)
        if(loggedIn == True):
            frame = getHindiMessage(msg="जारी रखें", frame=frame, x=150, y=300, color=green)
            frame = getHindiMessage(msg="लॉग आउट करें", frame=frame, x=360, y=300, color=red)
        else:
            frame = getHindiMessage(msg="लॉग इन करें", frame=frame, x=130, y=310, color=green)
            frame = getHindiMessage(msg="रद्द करें", frame=frame, x=390, y=310, color=red)


    return frame

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


def getHomepageKey(language, message="", loggedIn = False, fontSize = 1.2):

    result = getInput(determineKey, keyboardHomepageLayout, "homepage", (language, message, loggedIn, fontSize))
    return result


