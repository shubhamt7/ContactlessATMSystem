"""
This page is used to display welcome message to the user,
or message like Successful withdrawal, successful transfer,
Cancelled successfully, etc.
"""

import cv2
from objectDetection import getInput
from colors import red, green, white, black
from utility import getHindiMessage


def keyboardHomepageLayout(frame, language, message, loggedIn, fontSize):
    x = 20
    y = 50

    #Drawing heading outline
    cv2.rectangle(frame, (x, y), (x + 600, y + 120), black, 2)
    cv2.rectangle(frame, (x + 10, y + 10), (x + 590, y + 110), black, 2)

    #Drawing the keys
    x += 70
    cv2.rectangle(frame, (x, y + 200), (x + 200, y + 350), green, 2)
    cv2.rectangle(frame, (x + 250, y + 200), (x + 450, y + 350), red, 2)

    fontSize = 0.8

    # Messages to display, in case ENGLISH is the selected language
    messageColor = white
    if language == "english":
        if message == "transfer-success":
            message = "Money transferred successfully!"
        elif message == "withdraw-success":
            message = "Money withdrawn successfully"
        elif message == "cancelled-txn":
            message = "Transaction cancelled succesfully"
        elif message == "welcome-message":
            message = "Welcome to Contactless ATM!"
            fontSize = 1
        else:
            pass

    # Messages to display, in case HINDI is the selected language
    elif language == "hindi":
        if message == "transfer-success":
            message = "पैसा सफलतापूर्वक ट्रांसफर किया गया"
        elif message == "withdraw-success":
            message = "पैसा सफलतापूर्वक निकाला गया"
        elif message == "cancelled-txn":
            message = "सफलतापूर्वक रद्द किया गया"
        elif message == "welcome-message":
            message = "संपर्क रहित एटीएम में आपका स्वागत है!"
        else:
            pass
    else:
        pass

    #Deciding the text content of the keys depending upon the language, and the authentication status of user

    if language == "english":
        cv2.putText(frame, message, (50, 120), cv2.FONT_HERSHEY_SIMPLEX, fontSize, messageColor, 2)
        if loggedIn:
            cv2.putText(frame, "CONTINUE", (100, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.2, green, 2)
            cv2.putText(frame, "LOG OUT", (360, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.2, red, 2)
        else:
            cv2.putText(frame, "LOG IN", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.4, green, 2)
            cv2.putText(frame, "EXIT", (390, 340), cv2.FONT_HERSHEY_SIMPLEX, 1.4, red, 2)
    elif language == "hindi":
        frame = getHindiMessage(msg=message, frame=frame, x=50, y=90, color=messageColor)
        if loggedIn:
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


def getHomepageKey(language, message="", loggedIn=False, fontSize=1.2):
    result = getInput(determineKey, keyboardHomepageLayout, "homepage", (language, message, loggedIn, fontSize))
    return result
