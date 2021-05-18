import cv2
import time
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from colors import red, green, white, black, blue, yellow, cyanBlue, cyanGreen, cyanRed, mint, lightBlue, darkBlue
from utility import getHindiMessage

from utility import Fade

def timer(frame, t=20):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        cv2.putText(frame, timer, (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.8, red, 2)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    return "TIMEOUT"

def showInstructions(counterDuration):

    x = 20
    y = 80
    counter = counterDuration
    prevTime = time.time()
    messageColor = mint

    while counter > 0:

        frame = np.array([[darkBlue for x in range(650)] for y in range(500)],dtype="uint8")
        cv2.rectangle(frame, (x, 10), (x + 600, 80), black, 2)
        cv2.rectangle(frame, (x, y + 5), (x + 600, y + 350), black, 2)

        instructionsMessageEnglish = "PLEASE READ THE INSTRUCTIONS CAREFULLY"
        engMessage1 = "1. You need a pointed object of yellow"
        engMessage2 = "color for operating this machine"
        engMessage3 = "2. Please collect your money before leaving"
        engMessage4 = "3. This machine can't be operated if the"
        engMessage5 = "user is wearing yellow color"
        cv2.putText(frame, instructionsMessageEnglish, (x + 10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, red, 2)
        cv2.putText(frame, engMessage1, (40, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.8, messageColor, 2)
        cv2.putText(frame, engMessage2, (40, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.8, messageColor, 2)
        cv2.putText(frame, engMessage3, (40, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.8, messageColor, 2)
        cv2.putText(frame, engMessage4, (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, messageColor, 2)
        cv2.putText(frame, engMessage5, (40, 230), cv2.FONT_HERSHEY_SIMPLEX, 0.8, messageColor, 2)
        cv2.putText(frame, "Loading CATM in: ", (100, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 1)
        cv2.putText(frame, "seconds", (365, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 1)


        instructionsMessageHindi = "कृपया निर्देशों को ध्यान से पढ़ें"
        hindiMessage1 = "1. इस मशीन को चलाने के लिए आपको पीले रंग की एक"
        hindiMessage2 = "नुकीली वस्तु चाहिए"
        hindiMessage3 = "2. कृपया जाने से पहले अपने पैसे ले लें"
        hindiMessage4 = "3. यदि उपयोगकर्ता पीले रंग के कपड़े पहने हुए है तो यह मशीन"
        hindiMessage5 = "संचालित नहीं की जा सकती"

        frame = getHindiMessage(msg=instructionsMessageHindi, frame=frame, x=30, y=40, color=red)
        frame = getHindiMessage(msg=hindiMessage1, frame=frame, x=40, y=260, color=messageColor)
        frame = getHindiMessage(msg=hindiMessage2, frame=frame, x=40, y=290, color=messageColor)
        frame = getHindiMessage(msg=hindiMessage3, frame=frame, x=40, y=320, color=messageColor)
        frame = getHindiMessage(msg=hindiMessage4, frame=frame, x=40, y=350, color=messageColor)
        frame = getHindiMessage(msg=hindiMessage5, frame=frame, x=40, y=380, color=messageColor)


        cv2.putText(frame, str(counter), (330, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2)


        currTime = time.time()
        if (currTime - prevTime >= 1):
            prevTime = currTime
            counter = counter - 1

        cv2.imshow('Contactless ATM System', frame)

        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            return False

    Fade.fadeOut(frame)
    return True
