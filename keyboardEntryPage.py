import cv2
import numpy as np

def keyboardHomepageLayout(frame):
    x = 20
    y = 50

    cv2.rectangle(frame, (x, y), (x + 600, y + 100), (255, 255, 255), 2)
    cv2.rectangle(frame, (x + 150, y + 200), (x + 450, y + 350), (255, 255, 255), 2)


def determineEnterKey(cx, cy):
    if cy > 250 and cy < 400:
        if cx > 170 and cx < 470:
            return "enter"
        else:
            return ""

    else:
        return ""


def getEnterKey(message=""):
    cap = cv2.VideoCapture(0)
    count = 0

    result = ""
    while (1):

        ## Read the image
        ret, frame = cap.read()
        ## Do the processing
        frame = cv2.flip(frame, 1)

        cv2.putText(frame, message, (50, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        cv2.putText(frame, "ENTER", (235, 340), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 3)
        # cv2.putText(frame, "You entered: " + result, (50,440), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)

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
                        # print("diff- ",diff_area)
                        subs = determineEnterKey(cx, cy)
                        if (subs == ""):
                            pass
                        else:
                            # print(subs)
                            result += subs
                            break

        # display the keyboard in the screen

        keyboardHomepageLayout(frame)
        cv2.imshow('image', frame)
        if cv2.waitKey(1) == 27:  ## 27 - ASCII for escape key
            break
    ############################################

    ############################################
    ## Close and exit
    cap.release()
    cv2.destroyAllWindows()
    return result
    ############################################


