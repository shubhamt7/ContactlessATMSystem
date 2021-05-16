import pandas as pd
import cv2
from keyboardNumpad import getNumber
from screenshot import clickScreenshot

# Authentication
def authenticate():
    try:
        data = pd.read_csv('atmData.csv')
        ac = getNumber("Enter 6 digit Account number")
        user = data[data['ac'] == int(ac)]

        while(len(user) == 0 or len(ac) < 1):
            ac = getNumber("Wrong A/C No, Try again")
            user = data[data['ac'] == int(ac)]

        correctPin = int(user['pin'])

        pin = getNumber("Enter 4 digit PIN number")

        while len(pin) != 4 or (int(pin) != correctPin ):
            pin = getNumber("Wrong PIN! Try again")

        name = str(user['name'].values[0])
        clickScreenshot(name, ac)
        return ac  # ok

    except Exception as e:
        print(e)
