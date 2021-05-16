import cv2
import numpy as np
import time

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

    cap = CameraUtility.getInstance()
    count = 0
    result = ""
    fade = True
    while (1):

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        global cx
        global cy

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lowerMaskColor, upperMaskColor)
        blur = cv2.medianBlur(mask, 15)
        blur = cv2.GaussianBlur(blur, (5, 5), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        if len(contours) > 0:
            cnt = max(contours, key=cv2.contourArea)
            if (cv2.contourArea(cnt) > 100 and cv2.contourArea(cnt) < 1200):

                M = cv2.moments(cnt)

                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                cv2.circle(frame, (cx, cy), 1, (0, 0, 255), 2)

                count = count + 1
                if count == 20:
                    count = 0
                    subs = determineKey(cx, cy)
                    if (subs == ""):
                        pass
                    else:
                        result += subs
                        break

        keyboardHomepageLayout(frame, message, loggedIn, fontSize)
        if fade:
            Fade.fadeIn(frame)
            fade = False
        else:
            cv2.imshow('Contactless ATM System', frame)

        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break


    return result


