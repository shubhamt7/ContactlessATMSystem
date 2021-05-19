"""
Welcome page,
the foremost screen shown to the user with welcome message
"""

import cv2
import time
import numpy as np
from colors import white, black, blue
from utility import getHindiMessage
from utility import Fade


#Function for displaying welcome page to the user
#It takes number of seconds as an argument
def showWelcomePage(counterDuration):

    x = 20
    y = 80
    counter = counterDuration
    prevTime = time.time()
    welcomeMessageColor = white
    while counter > 0:

        frame = np.array([[black for x in range(650)] for y in range(500)],dtype="uint8")
        cv2.rectangle(frame, (x, y + 5), (x + 600, y + 350), white, 2)
        cv2.rectangle(frame, (x + 10, y + 15), (x + 590, y + 340), blue, 2)
        cv2.rectangle(frame, (x + 20, y + 25), (x + 580, y + 330), white, 2)

        welcomeMessageEnglish = "WELCOME TO CONTACTLESS ATM"
        cv2.putText(frame, welcomeMessageEnglish, (x + 120, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.7, welcomeMessageColor, 2)
        cv2.putText(frame, "Loading instructions in: ", (40, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 1)
        cv2.putText(frame, "seconds", (365, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 1)
        welcomeMessageHindi = "संपर्क रहित एटीएम में आपका स्वागत है"

        frame = getHindiMessage(msg=welcomeMessageHindi, frame=frame, x=140, y=270, color=welcomeMessageColor)
        cv2.putText(frame, str(counter), (340, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2)

        currTime = time.time()
        if currTime - prevTime >= 1:
            prevTime = currTime
            counter = counter - 1

        cv2.imshow('Contactless ATM System', frame)

        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            return False

    Fade.fadeOut(frame)
    return True
