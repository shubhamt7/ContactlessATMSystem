"""
This file contains the code for object detection logic
"""

from colors import lowerMaskColor, upperMaskColor, white, blue
import cv2
from screenshot import clickScreenshot
from utility import CameraUtility, Fade

def buildNumericString(subs, result):
    if subs == "quit":
        return result, "exit"
    elif subs == "":
        return result, "pass"
    elif subs == "backspace":
        if result == "":
            return result, "pass"
        else:
            result = result[:-1]
            return result, "ok"
    elif subs == "enter":
        if result == "":
            return result, "pass"
        else:
            return result, "break"
    else:
        if len(result) != 12:
            result += subs
            return result, "ok"


def getInput(determineKey, keyboardLayout, keyboardType, auxDetails = ()):

    cap = CameraUtility.getInstance()
    count = 0
    fade = True

    result = ""
    while 1:

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        if keyboardType == "numpad":
            cv2.putText(frame, "=> " , (55, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, blue, 2)
            cv2.putText(frame, result, (110, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)

        if keyboardType == "confirmation":
            language, type, name, amount, balance, recipient, displayDetails = auxDetails
            if type == "language":
                modifiedFrame = displayDetails(frame, "", type, name, amount, balance, recipient)
                frame = modifiedFrame
            else:
                frame = displayDetails(frame, language, type, name, amount, balance, recipient)

        global cx
        global cy

        #Filtering out all the colors except yellow
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lowerMaskColor, upperMaskColor)
        blur = cv2.medianBlur(mask, 15)
        blur = cv2.GaussianBlur(blur, (5, 5), 0)

        #Getting all the objects of yellow color
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        if len(contours) > 0:
            #Picking the object having largest area
            cnt = max(contours, key=cv2.contourArea)

            #Filtering extra small and extra large objects
            if cv2.contourArea(cnt) > 500 and cv2.contourArea(cnt) < 1200:


                #Finding centroid of the selected object
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                cv2.circle(frame, (cx, cy), 1, (0, 0, 255), 20)

                count = count + 1
                if count == 20:
                    count = 0

                    #Determining the key to press based on the position of the object
                    subs = determineKey(cx, cy)

                    if keyboardType == "numpad":
                        result, status = buildNumericString(subs, result)
                        if status == "break":
                            break
                        elif status == "exit":
                            exit(0)

                    else:
                        if subs == "":
                            pass
                        else:
                            result += subs
                            break


        #Displaying keyboard screens based on keyboard type
        if keyboardType == "homepage":
            language, message, loggedIn, fontSize = auxDetails
            frame = keyboardLayout(frame, language, message, loggedIn, fontSize)
        elif keyboardType == "confirmation":
            keyboardLayout(frame)
        elif keyboardType == "numpad":
            language, _, message = auxDetails
            frame = keyboardLayout(frame, language, message)
        else:
            language = auxDetails
            frame = keyboardLayout(frame, language)

        if fade:
            Fade.fadeIn(frame)
            fade = False
        else:
            cv2.imshow('Contactless ATM System', frame)
            # cv2.imshow('Mask', mask)

        if cv2.waitKey(1) == 27:
            cap.release()
            cv2.destroyAllWindows()
            return result

    #Taking the screenshot of user
    if keyboardType == "numpad":
        language, ac_no, _ = auxDetails
        if ac_no != "":
            clickScreenshot(ac_no)


    # Fade.fadeOut(frame)
    return result