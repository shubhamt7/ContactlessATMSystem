from colors import lowerMaskColor, upperMaskColor, white
import cv2
from screenshot import clickScreenshot
from utility import CameraUtility, Fade

def buildNumericString(subs, result):
    if (subs == "quit"):
        return result, "exit"
    elif (subs == ""):
        return result, "pass"
    elif subs == "backspace":
        if (result == ""):
            return result, "pass"
        else:
            result = result[:-1]
            return result, "ok"
    elif subs == "enter":
        if (result == ""):
            return result, "pass"
        else:
            return result, "break"
    else:
        if (len(result) != 12):
            result += subs
            return result, "ok"


def getInput(determineKey, keyboardLayout, keyboardType, auxDetails = ()):
    cap = CameraUtility.getInstance()
    count = 0
    fade = True

    result = ""
    while (1):

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        if(keyboardType == "numpad"):
            cv2.putText(frame, "You entered: " + result, (55, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)

        if(keyboardType == "confirmation"):
            type, name, amount, balance, recipient, displayDetails = auxDetails
            displayDetails(frame, type, name, amount, balance, recipient)

        global cx
        global cy

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lowerMaskColor, upperMaskColor)
        blur = cv2.medianBlur(mask, 15)
        blur = cv2.GaussianBlur(blur, (5, 5), 0)

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

                    subs = determineKey(cx, cy)
                    if(keyboardType == "numpad"):
                        result, status = buildNumericString(subs, result)
                        if (status == "break"):
                            break
                        elif (status == "exit"):
                            exit(0)
                    else:
                        if (subs == ""):
                            pass
                        else:
                            result += subs
                            break

        if(keyboardType == "homepage"):
            message, loggedIn, fontSize = auxDetails
            keyboardLayout(frame, message, loggedIn, fontSize)
        elif(keyboardType == "confirmation"):
            keyboardLayout(frame)
        elif(keyboardType == "numpad"):
            _, message = auxDetails
            keyboardLayout(frame, message)
        else:
            keyboardLayout(frame)

        if fade:
            Fade.fadeIn(frame)
            fade = False
        else:
            cv2.imshow('Contactless ATM System', frame)

        if cv2.waitKey(1) == 27:
            print("hello")
            cap.release()
            cv2.destroyAllWindows()
            return result

    if(keyboardType == "numpad"):
        ac_no, _ = auxDetails
        if (ac_no != ""):
            clickScreenshot(ac_no)


    Fade.fadeOut(frame)
    return result