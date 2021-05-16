"""
Keyboard for Selecting Action

Actions:
1. Withdrawing cash
2. Checking account balance
3. Cancelling the transaction

"""

import cv2
import numpy as np
from objectDetection import getInput
from colors import white, black, blue, lowerMaskColor, upperMaskColor


def keyboardActionLayout(frame):

    x = 120
    y = 130
    green = (0, 255, 0)

    cv2.rectangle(frame, (110, 20), (530, 110), black, 2)
    cv2.rectangle(frame, (115, 25), (525, 105), blue, 2)
    cv2.rectangle(frame, (120, 30), (520, 100), black, 2)

    cv2.rectangle(frame, (x - 10, y - 10), (530, 440), black, 2)
    cv2.rectangle(frame, (x - 5, y - 5), (525, 435), blue, 2)

    cv2.putText(frame, "CHOOSE AN ACTION", (x + 40, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)

    cv2.rectangle(frame, (x, y), (x + 200, y + 150), black, 2)
    cv2.putText(frame, "Withdraw", (x + 30, y + 80), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
    cv2.putText(frame, "Cash", (x + 30, y + 110), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)

    cv2.rectangle(frame, (x + 200, y), (x + 400, y + 150), black, 2)
    cv2.putText(frame, "Check", (x + 230, y + 80), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
    cv2.putText(frame, "Balance", (x + 230, y + 110), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)

    cv2.rectangle(frame, (x, y + 150), (x + 200, y + 300), black, 2)
    cv2.putText(frame, "Transfer", (x + 30, y + 230), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
    cv2.putText(frame, "Funds", (x + 30, y + 260), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)

    cv2.rectangle(frame, (x + 200, y + 150), (x + 400, y + 300), black, 2)
    cv2.putText(frame, "Cancel", (x + 220, y + 230), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
    cv2.putText(frame, "Transaction", (x + 220, y + 260), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)


def determineAction(cx, cy):

    if cy > 130 and cy < 280:
        if cx > 120 and cx < 320:
            return "withdraw"
        elif cx > 320 and cx < 520:
            return "balance"
        else:
            return ""
    elif cy > 280 and cy < 430:
        if cx > 120 and cx < 320:
            return "transfer"
        elif cx > 320 and cx < 520:
            return "cancel"
        else:
            return ""
    else:
        return ""

def getAction():

    result = getInput(determineAction, keyboardActionLayout, "action", ())
    return result


