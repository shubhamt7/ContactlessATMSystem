"""
This keyboard is used to display number pad
for taking numeric input from the user
e.g. Account number, PIN, amount, etc.
"""

import cv2
from colors import red, green, white, black, blue
from objectDetection import getInput
from utility import getHindiMessage


def keyboardNumpadLayout(frame, language, message):
    x = 50
    y = 60

    cv2.rectangle(frame, (x, 10), (x + 480, 50), black, 2)
    fontSize = 0.8

    # Message to be displayed if ENGLISH is the selected language
    if language == "english":
        if message == "enter-ac-no":
            cv2.putText(frame, "Enter your account number", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)
        elif message == "wrong-ac":
            cv2.putText(frame, "Wrong A/C number, try again", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)
        elif message == "enter-pin":
            cv2.putText(frame, "Enter your PIN", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)
        elif message == "wrong-pin":
            cv2.putText(frame, "Wrong pin, try again", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)
        elif message == "enter-amount":
            cv2.putText(frame, "Enter amount", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)
        elif message == "not-enough-balance":
            cv2.putText(frame, "Not enough balance, try again", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)
        elif message == "zero-amount":
            cv2.putText(frame, "Amount cannot be zero", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)
        elif message == "invalid-recipient":
            cv2.putText(frame, "Invalid recipient, enter again", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)
        elif message == "self-transfer":
            cv2.putText(frame, "Cannot transfer to self account", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white,
                        2)
        elif message == "enter-recipient":
            cv2.putText(frame, "Enter A/C no. of recipient", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)
        elif message == "invalid-denomination":
            cv2.putText(frame, "Enter in 100s/500s/2000s", (62, 40), cv2.FONT_HERSHEY_SIMPLEX, fontSize, white, 2)


    # Message to be displayed if HINDI is the selected language
    elif language == "hindi":
        if message == "enter-ac-no":
            frame = getHindiMessage(msg="अपना खाता नंबर दर्ज करें", frame=frame, x=60, y=10, color=white)
        elif message == "wrong-ac":
            frame = getHindiMessage(msg="गलत नंबर, फिर से दर्ज करें", frame=frame, x=60, y=10, color=white)
        elif message == "enter-pin":
            frame = getHindiMessage(msg="अपना पिन दर्ज करें", frame=frame, x=60, y=10, color=white)
        elif message == "wrong-pin":
            frame = getHindiMessage(msg="गलत पिन, फिर से दर्ज करें", frame=frame, x=60, y=10, color=white)
        elif message == "enter-amount":
            frame = getHindiMessage(msg="राशि दर्ज करें", frame=frame, x=60, y=10, color=white)
        elif message == "not-enough-balance":
            frame = getHindiMessage(msg="अपर्याप्त राशि, फिर से दर्ज करें", frame=frame, x=60, y=10, color=white)
        elif message == "zero-amount":
            frame = getHindiMessage(msg="राशि शून्य नहीं हो सकती", frame=frame, x=60, y=10, color=white)
        elif message == "invalid-recipient":
            frame = getHindiMessage(msg="अमान्य प्राप्तकर्ता, फिर से दर्ज करें", frame=frame, x=60, y=10, color=white)
        elif message == "self-transfer":
            frame = getHindiMessage(msg="स्वयं को ट्रांसफर नहीं कर सकते", frame=frame, x=60, y=10, color=white)
        elif message == "enter-recipient":
            frame = getHindiMessage(msg="प्राप्तकर्ता का खाता संख्या दर्ज करें", frame=frame, x=60, y=10, color=white)
        elif message == "invalid-denomination":
            frame = getHindiMessage(msg="कृपया 100/500/2000 के मूल्यवर्ग में दर्ज करें", frame=frame, x=60, y=10,
                                    color=white)

    else:
        exit(0)


    #Displaying the keys
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
    if language == "english":
        cv2.putText(frame, "DEL", (x + 30, y + 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, red, 2)
    elif language == "hindi":
        frame = getHindiMessage(msg="मिटाएं", frame=frame, x=x + 30, y=y + 40, color=red)

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
    if language == "english":
        cv2.putText(frame, "ENTER", (x + 20, y + 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, green, 2)
    elif language == "hindi":
        frame = getHindiMessage(msg="दर्ज करें", frame=frame, x=x + 20, y=y + 40, color=blue)

    x = 550
    y = 0

    cv2.rectangle(frame, (x, y), (x + 80, y + 50), (0, 0, 255), 2)
    cv2.putText(frame, " X ", (x + 12, y + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return frame


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


def getNumber(language, message="", ac_no=""):
    result = getInput(determineNumpadKey, keyboardNumpadLayout, "numpad", (language, str(ac_no), message))
    return result
