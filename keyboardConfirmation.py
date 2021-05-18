import cv2
import numpy as np
from objectDetection import getInput
from colors import red, green, white, black, lowerMaskColor, upperMaskColor
from utility import CameraUtility, getHindiMessage

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

def displayDetails(frame, language, type, name = "", amount = "", balance = "", recipient = ""):

    x = 20
    y = 50
    cv2.rectangle(frame, (x, y), (x + 600, y + 150), black, 2)

    if(language == "english" or language == ""):
        message1 = ""
        if type == "withdraw":
            message1 = "Dear customer, you are about to"
            message2 = "withdraw Rs." + str(amount) + " out of Rs. " + str(balance)
            cv2.putText(frame, message1, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2)
            cv2.putText(frame, message2, (50, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2)
            cv2.putText(frame, "CONFIRM", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 1)
            cv2.putText(frame, "CANCEL", (380, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        elif type == "language":
            message1 = "Please select your language"
            message2 = "कृपया अपनी भाषा चुनें"
            hindiChoice = "हिंदी"

            cv2.putText(frame, message1, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
            cv2.putText(frame, "ENGLISH", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 1)
            frame = getHindiMessage(msg=message2, frame=frame, x=50, y=130, color=white)
            frame = getHindiMessage(msg=hindiChoice, frame=frame, x=420, y=310, color=red)
            return frame

        elif type == "transfer":
            message1 = "Dear customer, you are about to"
            message2 = "transfer Rs." + str(amount) + " out of Rs." + str(balance)
            message3 = "to account number " + recipient
            cv2.putText(frame, message1, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2)
            cv2.putText(frame, message2, (50, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2)
            cv2.putText(frame, message3, (50, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.8, white, 2)
            cv2.putText(frame, "CONFIRM", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 1)
            cv2.putText(frame, "CANCEL", (380, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2)

        elif type == "account-type" or type == "retry-account-type":
            if(type == "account-type"):
                message = "Select your account type"
            else:
                message = "Wrong account type, select again"

            cv2.putText(frame, message, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
            cv2.putText(frame, "Savings A/C", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.8, green, 1)
            cv2.putText(frame, "Current A/C", (360, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        # action confirmation
        else:
            if type == "withdraw-action":
                message1 = "Continue withdrawing money"
            elif type == "transfer-action":
                message1 = "Continue transferring money"
            elif type == "balance-action":
                message1 = "Continue checking balance"
            elif type == "cancel-action":
                message1 = "Continue cancelling the transaction"

            message2 = "or perform any other action"

            cv2.putText(frame, message1, (50, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
            cv2.putText(frame, message2, (50, 145), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
            cv2.putText(frame, "CONTINUE", (110, 330), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 1)
            cv2.putText(frame, "CHANGE", (370, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2)
            cv2.putText(frame, "ACTION", (370, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2)

    #language = hindi
    else:
        message1 = ""
        if type == "withdraw":
            message1 = "प्रिय ग्राहक, आप अपने अकाउंट बैलेंस " + str(balance) + " में से "
            message2 = str(amount) + " रुपये निकालने जा रहे हैं"
            message3 = "पुष्टि करें"
            message4 = "रद्द करें"
            frame = getHindiMessage(msg=message1, frame=frame, x=50, y=100, color=white)
            frame = getHindiMessage(msg=message2, frame=frame, x=50, y=130, color=white)
            frame = getHindiMessage(msg=message3, frame=frame, x=150, y=300, color=white)
            frame = getHindiMessage(msg=message4, frame=frame, x=390, y=300, color=red)

            # cv2.putText(frame, message1, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
            # cv2.putText(frame, message2, (50, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
            # cv2.putText(frame, "CONFIRM", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 1)
            # cv2.putText(frame, "CANCEL", (380, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        elif type == "language":
            message1 = "Please select your language"
            message2 = "कृपया अपनी भाषा चुनें"
            hindiChoice = "हिंदी"

            cv2.putText(frame, message1, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2)
            cv2.putText(frame, "ENGLISH", (120, 340), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 1)
            frame = getHindiMessage(msg=message2, frame=frame, x=50, y=130, color=white)
            frame = getHindiMessage(msg=hindiChoice, frame=frame, x=420, y=310, color=white)
            return frame

        elif type == "transfer":
            message1 = "प्रिय ग्राहक, आप खाता संख्या " + str(recipient) + " को " + str(amount) + " रुपये "
            message2 = "ट्रांसफर करने वाले हैं"
            message3 = "पुष्टि करें"
            message4 = "रद्द करें"

            frame = getHindiMessage(msg=message1, frame=frame, x=50, y=100, color=white)
            frame = getHindiMessage(msg=message2, frame=frame, x=50, y=130, color=white)
            frame = getHindiMessage(msg=message3, frame=frame, x=150, y=300, color=white)
            frame = getHindiMessage(msg=message4, frame=frame, x=390, y=300, color=red)

        elif type == "account-type" or type == "retry-account-type":
            if (type == "account-type"):
                message = "खाता प्रकार चुनें"
            else:
                message = "गलत प्रकार चुना गया, पुनः प्रयास करें"

            frame = getHindiMessage(msg=message, frame=frame, x=50, y=100, color=white)
            frame = getHindiMessage(msg="बचत खाता", frame=frame, x=120, y=300, color=white)
            frame = getHindiMessage(msg="चालू खाता", frame=frame, x=380, y=300, color=white)

        # action confirmation
        else:
            if type == "withdraw-action":
                message1 = "पैसे निकालना जारी रखें"
            elif type == "transfer-action":
                message1 = "पैसे ट्रांसफर करना जारी रखें"
            elif type == "balance-action":
                message1 = "बैलेंस चेक करना जारी रखें"
            elif type == "cancel-action":
                message1 = "रद्द करना जारी रखें"

            message2 = " या कोई अन्य कार्य करें"

            frame = getHindiMessage(msg=message1 + message2, frame=frame, x=50, y=110, color=white)
            # frame = getHindiMessage(msg=message2, frame=frame, x=50, y=145, color=white)
            frame = getHindiMessage(msg="जारी रखें", frame=frame, x=135, y=300, color=white)
            frame = getHindiMessage(msg="अन्य कार्य करें", frame=frame, x=370, y=300, color=white)
            # frame = getHindiMessage(msg="करें", frame=frame, x=370, y=320, color=white)

    return frame

def getConfirmation(language, type, name = "",amount = "", balance = "", recipient = ""):

    result = getInput(determineConfirmationKey, keyboardConfirmationLayout, "confirmation", (language, type, name, amount, balance,recipient,displayDetails))
    return result
