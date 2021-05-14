import pandas as pd
import cv2
from keyboardNumpad import getNumber

# Authentication
def authenticate():
    try:
        data = pd.read_csv('atmData.csv')
        ac = getNumber("Enter 6 digit Account number")
        user = data[data['ac'] == int(ac)]

        while(len(user) == 0 or len(ac) < 6):
            return "WAC"  # wrong acc number


        correctPin = int(user['pin'])

        pin = getNumber("Enter 4 digit PIN number")

        while len(pin) != 4:
            pin = getNumber("Enter 4 digit PIN number")

        if (int(pin) != correctPin):
            return "WPIN"

        return ac  # ok

    except Exception as e:
        print(e)