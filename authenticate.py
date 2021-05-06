import pandas as pd
from keyboardNumpad import getNumber

# Authentication
def authenticate():
    try:
        data = pd.read_csv('atmData.csv')
        ac = getNumber("Enter 6 digit Account number")

        while len(ac) != 6:
            ac = getNumber("Enter 6 digit Account number")

        person = data[data['ac'] == int(ac)]

        if (len(person) == 0):
            return "WAC"  # wrong acc number

        correctPin = int(person['pin'])

        pin = getNumber("Enter 4 digit PIN number")

        while len(pin) != 4:
            pin = getNumber("Enter 4 digit PIN number")

        if (int(pin) != correctPin):
            return "WPIN"

        return ac  # ok

    except Exception as e:
        print(e)