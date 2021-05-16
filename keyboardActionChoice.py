"""
Keyboard for Selecting Action

Actions:
1. Withdrawing cash
2. Checking account balance
3. Cancelling the transaction

"""

import cv2
import numpy as np
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

    cap = cv2.VideoCapture(0)
    count = 0

    result = ""
    while (1):

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        global cx
        global cy
        # global old_area, new_area
        # old_area, new_area = 0, 0

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lowerMaskColor, upperMaskColor)
        blur = cv2.medianBlur(mask, 15)
        blur = cv2.GaussianBlur(blur, (5, 5), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        if len(contours) > 0:
            cnt = max(contours, key=cv2.contourArea)
            if (cv2.contourArea(cnt) > 600 and cv2.contourArea(cnt) < 1200):

                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                cv2.circle(frame, (cx, cy), 1, (0, 0, 255), 2)
                count = count + 1
                if count == 20:
                    count = 0
                    subs = determineAction(cx, cy)
                    if (subs == ""):
                        pass
                    else:
                        result += subs
                        break

        keyboardActionLayout(frame)
        cv2.imshow('Contactless ATM System', frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return result


