import cv2
import numpy as np

from colors import red, green, white, black

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
    cap = cv2.VideoCapture(0)
    count = 0

    result = ""
    while (1):

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        if(type == "instructions"):
            displayDetails(frame, type)
        # elif(type == "quit"):
        #     displayDetails(frame, type)
        elif(type == "withdraw"):
            displayDetails(frame, type, name, amount, balance)
        else:
            displayDetails(frame, type, name, amount, balance, recipient)

        global cx
        global cy
        # global old_area, new_area
        # old_area, new_area = 0, 0
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([14, 141, 140])
        upper_yellow = np.array([84, 255, 255])

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
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
                    subs = determineConfirmationKey(cx, cy)
                    if (subs == ""):
                        pass
                    else:
                        result += subs
                        break

        keyboardConfirmationLayout(frame)
        cv2.imshow('Contactless ATM System', frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return result
