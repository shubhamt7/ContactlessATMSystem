"""
Code for authenticating a user before
he is allowed to perform any other operations.

The user is asked to enter account number and pin
"""


import pandas as pd
from keyboardNumpad import getNumber

def authenticate(language):
    try:
        data = pd.read_csv('atmData.csv')
        ac = getNumber(language, "enter-ac-no")
        user = data[data['ac'] == int(ac)]

        while(len(user) == 0 or len(ac) < 1):
            ac = getNumber(language, "wrong-ac")
            user = data[data['ac'] == int(ac)]

        correctPin = int(user['pin'])

        counter = 3
        pin = getNumber(language, "enter-pin", ac)

        while len(pin) != 4 or (int(pin) != correctPin ):
            counter = counter - 1
            if(counter == 0):
                exit(0)
            pin = getNumber(language, "wrong-pin-" + str(counter))

        return ac  # ok

    except Exception as e:
        print(e)
