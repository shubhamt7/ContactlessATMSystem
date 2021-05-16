import cv2
import numpy as np
from objectDetection import getInput
from colors import red, green, white, black, lowerMaskColor, upperMaskColor
from utility import CameraUtility

# black = (0, 0, 0)
# white = (255, 255, 255)
# green = (0, 200, 0)
# red = (0, 0, 200)
# blue = (255, 0, 0)

def keyboardConfirmationLayout(frame):

    x = 90
    y = 50
    cv2.rectangle(frame, (x, y + 200), (x + 200, y + 350), green, 2)
    cv2.rectangle(frame, (x + 250, y + 200), (x + 450, y + 350), red, 2)

def determineConfirmationKey(cx, cy):
    if cy > 250 and cy < 400:
        if cx > 90 and cx < 290:
            return "choice1"
        elif cx > 340 and cx < 540:
            return "choice2"
        else:
            return ""

    else:
        return ""

def displayDetails(frame, type, name = "", amount = "", balance = "", recipient = ""):

    x = 20
    y = 50
    message1 = ""

    if type == "withdraw":
        cv2.rectangle(frame, (x, y), (x + 600, y + 150), black, 2)
        message1 = "Hello " + name + "!, " + "You are about"
        message2 = "to withdraw " + str(amount) + " out of " + str(balance)
        cv2.putText(frame, message1, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
        cv2.putText(frame, message2, (50, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
        cv2.putText(frame, "CONFIRM", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 1)
        cv2.putText(frame, "CANCEL", (380, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    elif type == "transfer":
        cv2.rectangle(frame, (x, y), (x + 600, y + 150), black, 2)
        message1 = "Hello " + name + "!, " + "You are about"
        message2 = "to transfer " + str(amount) + " out of " + str(balance)
        message3 = "to " + recipient
        cv2.putText(frame, message1, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
        cv2.putText(frame, message2, (50, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
        cv2.putText(frame, message3, (50, 160), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
        cv2.putText(frame, "CONFIRM", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 1)
        cv2.putText(frame, "CANCEL", (380, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2)

    elif type == "account-type" or type == "retry-account-type":
        if(type == "account-type"):
            message = "Select your account type"
        else:
            message = "Wrong account type, select again"

        cv2.rectangle(frame, (x, y), (x + 600, y + 150), black, 2)
        cv2.putText(frame, message, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
        cv2.putText(frame, "Savings A/C", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.8, green, 1)
        cv2.putText(frame, "Current A/C", (380, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # action confirmation
    else:
        cv2.rectangle(frame, (x, y), (x + 600, y + 150), black, 2)
        if type == "withdraw-action":
            message1 = "Continue with withdrawing money"
        elif type == "transfer-action":
            message1 = "Continue with transferring money"
        elif type == "balance-action":
            message1 = "Continue to check balance"
        elif type == "cancel-action":
            message1 = "Continue to cancel the transaction"

        message2 = "or perform any other action"

        cv2.putText(frame, message1, (50, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
        cv2.putText(frame, message2, (50, 145), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
        cv2.putText(frame, "CONTINUE", (110, 330), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 1)
        cv2.putText(frame, "CHANGE", (370, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2)
        cv2.putText(frame, "ACTION", (370, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2)


def getConfirmation(type, name = "",amount = "", balance = "", recipient = ""):

    result = getInput(determineConfirmationKey, keyboardConfirmationLayout, "confirmation", (type, name, amount, balance,recipient,displayDetails))
    return result
