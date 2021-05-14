import cv2
import numpy as np
from colors import red, green, white, black, blue

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


def getNumber(message=""):
    cap = cv2.VideoCapture(0)
    count = 0

    result = ""
    while (1):

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.putText(frame, "You entered: " + result, (55, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)

        global cx
        global cy
        global old_area, new_area
        old_area, new_area = 0, 0
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([14, 141, 140])
        upper_yellow = np.array([84, 255, 255])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        blur = cv2.medianBlur(mask, 15)
        blur = cv2.GaussianBlur(blur, (5, 5), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame, contours, -1, green, 2)

        if len(contours) > 0:
            cnt = max(contours, key=cv2.contourArea)
            if (cv2.contourArea(cnt) > 600 and cv2.contourArea(cnt) < 1200):

                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                new_area = cv2.contourArea(cnt)
                cv2.circle(frame, (cx, cy), 1, (0, 0, 255), 2)
                if count == 0:
                    old_area = new_area
                count = count + 1
                if count == 20:
                    count = 0
                    diff_area = new_area - old_area
                    if diff_area > 500 and diff_area < 1200:
                        subs = determineNumpadKey(cx, cy)
                        if(subs == "quit"):
                            exit(0)
                        elif (subs == ""):
                            pass
                        elif subs == "backspace":
                            if (result == ""):
                                pass
                            else:
                                result = result[:-1]

                        elif subs == "enter":
                            if(result == ""):
                                pass
                            else:
                                break

                        else:
                            result += subs



        keyboardNumpadLayout(frame, message)
        cv2.imshow('Contactless ATM System', frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    return result

