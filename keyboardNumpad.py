import cv2
import numpy as np
from screenshot import clickScreenshot
from colors import red, green, white, black, lowerMaskColor, upperMaskColor
from objectDetection import buildNumericString
from objectDetection import getInput

def keyboardNumpadLayout(frame, message):
    x = 50
    y = 60

    cv2.rectangle(frame, (x, 10), (x + 480, 50), black, 2)
    cv2.putText(frame, message, (52, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
    cv2.rectangle(frame, (x, y), (x + 480, y + 400), black, 2)

    # 1, 2, 3

    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "1", (x + 40, y + 80), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, white, 2)
    x += 120

    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "2", (x + 40, y + 80), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, white, 2)
    x += 120

    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "3", (x + 40, y + 80), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, white, 2)
    x += 120

    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "4", (x + 40, y + 80), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, white, 2)
    x += 120

    # 4, 5, 6
    y += 120

    x = 50
    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "5", (x + 40, y + 80), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, white, 2)
    x += 120

    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "6", (x + 40, y + 80), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, white, 2)
    x += 120

    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "7", (x + 40, y + 80), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, white, 2)
    x += 120

    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "DEL", (x + 30, y + 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, red, 2)
    x += 120

    # 7, 8, 9
    y += 120
    x = 50
    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "8", (x + 40, y + 80), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, white, 2)
    x += 120

    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "9", (x + 40, y + 80), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, white, 2)
    x += 120

    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "0", (x + 40, y + 80), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, white, 2)
    x += 120

    cv2.rectangle(frame, (x, y), (x + 120, y + 120), black, 2)
    cv2.putText(frame, "ENTER", (x + 20, y + 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, green, 2)

    x = 550
    y = 0

    cv2.rectangle(frame, (x, y), (x + 80, y + 50), (0, 0, 255), 2)
    cv2.putText(frame, "Quit", (x + 10, y + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


def determineNumpadKey(cx, cy):
    if cy > 50 and cy < 410 and cx > 50 and cx < 530:
        # first row  1,2,3,4
        if cy > 50 and cy < 170:
            # 1
            if cx > 50 and cx < 170:
                return "1"
            # 2
            elif cx > 170 and cx < 290:
                return "2"
            # 3
            elif cx > 270 and cx < 410:
                return "3"
            # 4
            else:
                return "4"


        # second row 5,6,7,backspace

        elif cy > 170 and cy < 290:
            # 5
            if cx > 50 and cx < 170:
                return "5"

            # 6
            elif cx > 170 and cx < 290:
                return "6"

            # 7
            elif cx > 290 and cx < 410:
                return "7"

            # Backspace
            else:
                return "backspace"


        # third row 8,9,0, Enter
        elif cy > 290 and cy < 410:

            # 8
            if cx > 50 and cx < 170:
                return "8"

            # 9
            elif cx > 170 and cx < 290:
                return "9"

            # 0
            elif cx > 290 and cx < 410:
                return "0"

            # Enter
            else:
                return "enter"

        else:
            return ""

    elif cx > 550 and cx < 630 and cy > 0 and cy < 50:
        return "quit"

    else:
        return ""


def getNumber(message="", ac_no = ""):

    result = getInput(determineNumpadKey, keyboardNumpadLayout, "numpad", (str(ac_no), message))
    return result

