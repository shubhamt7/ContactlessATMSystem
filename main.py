import pandas as pd
from keyboardNumpad import getNumber
from keyboardHomepage import getHomepageKey
from keyboardConfirmation import getConfirmation
from keyboardActionChoice import getAction
from authenticate import authenticate



def runCATM(message=""):
    try:
        entryPageInput = getHomepageKey(message)

        if(entryPageInput == "exit"):
            exit(0)

        elif (entryPageInput == "enter"):
            authResult = authenticate()
            if (authResult == "WAC"):
                message = "Wrong account number, try again!"
                runCATM(message)
            elif (authResult == "WPIN"):
                message = "Wrong PIN, try again!"
                runCATM(message)
            else:
                ac_no = int(authResult)
                data = pd.read_csv('atmData.csv')
                person = data[data['ac'] == ac_no]
                print(person)
                name = str(person['name'].values[0])

                action = getAction()
                actionConfirmation = getConfirmation(action + "-action")
                while(actionConfirmation != "confirm"):
                    action = getAction()
                    actionConfirmation = getConfirmation(action + "-action")

                if (action == "withdraw"):
                    amount = int(getNumber("Enter amount to withdraw"))
                    balance = int(person['balance'])

                    while (amount > balance):
                        amount = int(getNumber("Not enough money, enter again"))

                    confirmationMessage = getConfirmation("withdraw", name, amount, balance)
                    if (confirmationMessage == "confirm"):
                        newBalance = balance - amount
                        data.loc[data['ac'] == ac_no, 'balance'] = newBalance
                        data.to_csv('atmData.csv', index=False)

                        runCATM("Successfull")
                    else:
                        runCATM("Transaction cancelled")

                # runCATM("Successfull")

                elif (action == "balance"):
                    balance = person['balance']
                    runCATM("Your balance is: " + str(int(balance)))
                    # print(balance)

                elif (action == "transfer"):

                    data = pd.read_csv('atmData.csv')

                    # ac = getNumber("Enter 6 digit Account number")
                    # user = data[data['ac'] == int(ac)]
                    #
                    # while (len(user) == 0 or len(ac) < 6):
                    #     return "WAC"  # wrong acc number

                    transfer_to = getNumber("Enter A/C no of recipient")
                    recipient = data[data['ac'] == int(transfer_to)]

                    while(len(recipient) == 0 or len(transfer_to) < 6):
                        transfer_to = getNumber("Invalid recipient, try again.")

                    while(int(transfer_to) == ac_no):
                        transfer_to = getNumber("Can't transfer to own account")

                    currUserBalance = int(person['balance'])

                    amount = int(getNumber("Enter amount to tranfer"))
                    while (amount > currUserBalance):
                        amount = int(getNumber("Not enough money, enter again"))

                    while (amount == 0):
                        amount = int(getNumber("Amount can't be zero"))

                    recipientBalance = int(recipient['balance'])
                    recipientName = str(recipient['name'].values[0])


                    confirmationMessage = getConfirmation("transfer", name, amount, currUserBalance, recipientName)

                    if (confirmationMessage == "confirm"):
                        currUserBalance = currUserBalance - amount
                        recipientBalance = recipientBalance + amount
                        data.loc[data['ac'] == ac_no, 'balance'] = currUserBalance
                        data.loc[data['ac'] == int(transfer_to), 'balance'] = recipientBalance
                        data.to_csv('atmData.csv', index=False)

                        runCATM("Successfull")
                    else:
                        runCATM("Transaction cancelled")

                elif action == "cancel":
                    message = "Transaction cancelled"
                    runCATM(message)
    except Exception as e:
        print(e)

try:
    runCATM("Welcome to Contactless ATM")
except Exception as e:
    print(e)

# try:
#     getConfirmation('transfer')
# except Exception as e:
#     print(e)
#
# try:
#     getAction()
# except Exception as e:
#     print(e)

# try:
#     getNumber("Enter something")
# except Exception as e:
#     print(e)