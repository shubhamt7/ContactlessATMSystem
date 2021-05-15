import pandas as pd
from keyboardNumpad import getNumber
from keyboardHomepage import getHomepageKey
from keyboardConfirmation import getConfirmation
from keyboardActionChoice import getAction
from authenticate import authenticate
from instructionsPage import showInstructions

def runActions(authResult):

    ac_no = int(authResult)
    data = pd.read_csv('atmData.csv')
    person = data[data['ac'] == ac_no]
    print(person)
    name = str(person['name'].values[0])
    action = getAction()

    actionConfirmation = getConfirmation(action + "-action")
    while (actionConfirmation != "choice1"):
        action = getAction()
        actionConfirmation = getConfirmation(action + "-action")

    if (action == "withdraw"):
        amount = int(getNumber("Enter amount to withdraw"))
        balance = int(person['balance'])

        while (amount > balance):
            amount = int(getNumber("Not enough money, enter again"))

        confirmationMessage = getConfirmation("withdraw", name, amount, balance)
        if (confirmationMessage == "choice1"):
            newBalance = balance - amount
            data.loc[data['ac'] == ac_no, 'balance'] = newBalance
            data.to_csv('atmData.csv', index=False)

            runCATM("Successfully withdrawn", authResult)
        else:
            runCATM("Transaction cancelled", authResult)

    # runCATM("Successfull")

    elif (action == "balance"):
        balance = person['balance']
        runCATM("Your balance is: " + str(int(balance)), authResult)
        # print(balance)

    elif (action == "transfer"):

        data = pd.read_csv('atmData.csv')
        transfer_to = getNumber("Enter A/C no of recipient")
        recipient = data[data['ac'] == int(transfer_to)]

        while (len(recipient) == 0 or len(transfer_to) < 6):
            transfer_to = getNumber("Invalid recipient, try again.")
            recipient = data[data['ac'] == int(transfer_to)]

        while (int(transfer_to) == ac_no):
            transfer_to = getNumber("Can't transfer to own account")
            recipient = data[data['ac'] == int(transfer_to)]

        currUserBalance = int(person['balance'])

        amount = int(getNumber("Enter amount to tranfer"))
        while (amount > currUserBalance):
            amount = int(getNumber("Not enough money, enter again"))

        while (amount == 0):
            amount = int(getNumber("Amount can't be zero"))

        recipientBalance = int(recipient['balance'])
        recipientName = str(recipient['name'].values[0])

        confirmationMessage = getConfirmation("transfer", name, amount, currUserBalance, recipientName)

        if (confirmationMessage == "choice1"):
            currUserBalance = currUserBalance - amount
            recipientBalance = recipientBalance + amount
            data.loc[data['ac'] == ac_no, 'balance'] = currUserBalance
            data.loc[data['ac'] == int(transfer_to), 'balance'] = recipientBalance
            data.to_csv('atmData.csv', index=False)

            runCATM("Successfully Transferred", authResult)
        else:
            runCATM("Transaction cancelled", authResult)

    elif action == "cancel":
        message = "Transaction cancelled"
        runCATM(message, authResult)


def runCATM(message="", accountNo = "", fontSize = 1.2):
    try:

        if(accountNo == ""):
            loggedIn = False
            # showInstructions()
        else:
            loggedIn = True

        entryPageInput = getHomepageKey(message, loggedIn, fontSize)

        if(entryPageInput == "exit"):
            exit(0)

        elif (entryPageInput == "enter"):
            if(accountNo != ""):
                runActions(accountNo)

            authResult = authenticate()
            # authenticationResult = authResult
            ac_no = int(authResult)
            runActions(authResult)

    except Exception as e:
        print(e)

try:
    runCATM("Welcome to Contactless ATM")
except Exception as e:
    print(e)


# try:
#     showInstructions()
# except Exception as e:
#     print(e)

# try:
#     print(getNumber("Enter something"))
# except Exception as e:
#     print(e)
#
# try:
#     getHomepageKey(message = "Welcome to CATM System", loggedIn = True)
# except:
#     print("Error")

# try:
#     authenticate()
# except Exception as e:
#     print(e)