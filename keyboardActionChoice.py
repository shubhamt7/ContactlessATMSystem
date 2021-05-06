"""
Keyboard for Selecting Action

Actions:
1. Withdrawing cash
2. Checking account balance
3. Cancelling the transaction

"""

import cv2
import numpy as np

def keyboardActionLayout(frame):
    x = 20
    y = 150

    # 20 se 220,
    # 220 se 420
    # 420 se 620

    cv2.rectangle(frame, (x, y), (x + 200, y + 150), (0, 255, 0), 2)
    cv2.putText(frame, "Withdraw", (x + 10, y + 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, "Cash", (x + 10, y + 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.rectangle(frame, (x + 200, y), (x + 400, y + 150), (0, 255, 0), 2)
    cv2.putText(frame, "Check", (x + 210, y + 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, "Balance", (x + 210, y + 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.rectangle(frame, (x + 400, y), (x + 600, y + 150), (0, 255, 0), 2)
    cv2.putText(frame, "Cancel", (x + 420, y + 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, "Transaction", (x + 420, y + 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

def determineAction(cx, cy):
    if cy > 150 and cy < 300:
        if cx > 20 and cx < 220:
            return "w"
        elif cx > 220 and cx < 420:
            return "c"
        elif cx > 420 and cx < 620:
            return "t"
        else:
            return ""

    else:
        return ""

def getAction():
    cap = cv2.VideoCapture(0)
    count = 0

    result = ""
    while (1):

        ## Read the image
        ret, frame = cap.read()
        ## Do the processing
        frame = cv2.flip(frame, 1)

        global cx
        global cy
        global old_area, new_area
        old_area, new_area = 0, 0
        # for yellow color idenitfiaction in frame
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([14, 141, 140])  # change this hsv values if yellow color as per your lighting condition
        upper_yellow = np.array([84, 255, 255])  # same as above

        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        blur = cv2.medianBlur(mask, 15)
        blur = cv2.GaussianBlur(blur, (5, 5), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        cv2.imshow("mask", mask)
        # find contours in frame
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # function to determine which key is pressed based on the center of the contour(yellow paper)

        cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

        if len(contours) > 0:
            cnt = max(contours, key=cv2.contourArea)
            if (cv2.contourArea(cnt) > 600 and cv2.contourArea(cnt) < 1200):

                M = cv2.moments(cnt)

                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                # print ("Centroid = ", cx, ", ", cy)
                new_area = cv2.contourArea(cnt)
                # print("new area ",new_area)
                cv2.circle(frame, (cx, cy), 1, (0, 0, 255), 2)
                if count == 0:
                    old_area = new_area
                    # print("in count==0   ",count)

                count = count + 1
                # print(count)
                if count == 20:
                    count = 0
                    diff_area = new_area - old_area
                    if diff_area > 500 and diff_area < 1200:
                        subs = determineAction(cx, cy)
                        if (subs == ""):
                            pass
                        else:
                            result += subs
                            break
                        cv2.putText(frame, "Enter name: " + result, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        keyboardActionLayout(frame)
        cv2.imshow('image', frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return result


