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
            ac = getNumber("Wrong A/C No, Try again")
            user = data[data['ac'] == int(ac)]

        correctPin = int(user['pin'])

        pin = getNumber("Enter 4 digit PIN number")

        while len(pin) != 4 or (int(pin) != correctPin):
            pin = getNumber("Wrong PIN! Try again")

        return ac  # ok

    except Exception as e:
        print(e)