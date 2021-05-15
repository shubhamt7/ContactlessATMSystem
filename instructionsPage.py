import cv2
import time

from colors import red, green, white, black, blue, yellow

def timer(frame, t = 20):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        cv2.putText(frame, timer, (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.8, red, 2)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    return "TIMEOUT"


def showInstructions(counterDuration):

    cap = cv2.VideoCapture(0)
    x = 20
    y = 80
    counter = counterDuration

    prevTime = time.time()
    while counter > 0:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        cv2.rectangle(frame, (x, 10), (x + 600, 75), black, 2)
        cv2.rectangle(frame, (x, y), (x + 600, y + 300), black, 2)
        message1 = "1. You need a pointed object of yellow"
        message2 = "color for operating this machine"
        message3 = "2. Please collect your money before leaving"
        message4 = "3. This machine can't be operated if the"
        message5 = "user is wearing yellow color"

        cv2.putText(frame, "PLEASE READ THE INSTRUCTIONS CAREFULLY", (x + 10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, red, 2)
        cv2.putText(frame, message1, (40, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.8, green, 2)
        cv2.putText(frame, message2, (40, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.8, green, 2)
        cv2.putText(frame, message3, (40, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.8, green, 2)
        cv2.putText(frame, message4, (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, green, 2)
        cv2.putText(frame, message5, (40, 230), cv2.FONT_HERSHEY_SIMPLEX, 0.8, green, 2)

        cv2.putText(frame, "Loading CATM in " + str(counter) + " seconds..", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 1)

        currTime = time.time()
        if(currTime - prevTime >= 1):
            prevTime = currTime
            counter = counter - 1

        cv2.imshow('Contactless ATM System', frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
