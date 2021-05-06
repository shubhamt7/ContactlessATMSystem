import pandas as pd
from keyboardNumpad import getNumber
from keyboardEntryPage import getEnterKey
from keyboardConfirmation import getConfirmation
from keyboardActionChoice import getAction
from authenticate import authenticate


def runCATM(message=""):
    try:
        ans1 = getEnterKey(message)
        if (ans1 == "enter"):
            auth = authenticate()
            if (auth == "WAC"):
                message = "Wrong account number, try again!"
                runCATM(message)
            elif (auth == "WPIN"):
                message = "Wrong PIN, try again!"
                runCATM(message)
            else:
                ac_no = int(auth)
                print(auth)

                data = pd.read_csv('atmData.csv')
                person = data[data['ac'] == ac_no]
                print(person)
                name = str(person['name'].values[0])

                WC_option = getAction()
                if (WC_option == "w"):
                    amount = int(getNumber("Enter amount to withdraw"))
                    balance = int(person['balance'])

                    while (amount > balance):
                        amount = int(getNumber("Not enough money, enter again"))

                    msg = getConfirmation(name, amount, balance)
                    if (msg == "confirm"):
                        newBalance = balance - amount
                        data.loc[data['ac'] == ac_no, 'balance'] = newBalance
                        data.to_csv('atmData.csv', index=False)

                        runCATM("Successfull")
                    else:
                        runCATM("Transaction cancelled")

                # runCATM("Successfull")

                elif (WC_option == "c"):
                    balance = person['balance']
                    runCATM("Your balance is: " + str(int(balance)))
                    print(balance)

                else:
                    message = "Transaction cancelled"
                    runCATM(message)
    except Exception as e:
        print(e)

try:
    runCATM("Welcome to CATM system")
except Exception as e:
    print(e)