import pandas as pd
from keyboardNumpad import getNumber
from keyboardHomepage import getHomepageKey
from keyboardConfirmation import getConfirmation
from keyboardActionChoice import getAction
from authenticate import authenticate
from instructionsPage import showInstructions
from screenshot import getCurrentDateAndTime

def logTransaction(type, currentUserName = "", curr_ac_no = "", amount = "", recipientName = "", recipient_ac_no = ""):

    currentDate, currentTime = getCurrentDateAndTime()
    fileName = str(currentDate) + ".txt"

    if(type == "transfer"):
        transactionDetails = currentUserName + " (" + curr_ac_no + ") transferred Rs. " + amount + " to " + recipientName \
                             + " (" + recipient_ac_no + ") at " + str(currentTime)
    else: #withdraw
        transactionDetails = currentUserName + " (" + curr_ac_no + ") withdrew Rs. " + amount + " at " + str(currentTime)

    with open(fileName, "a+") as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        f.write(transactionDetails)

def getAccountDetails(account_no):
    ac_no = int(account_no)
    data = pd.read_csv('atmData.csv')
    person = data[data['ac'] == ac_no]
    name = str(person['name'].values[0])
    account_type = str(person['account_type'].values[0])

    return ac_no, name, account_type

def selectAccountType(actual_account_type):
    choice = getConfirmation("account-type")
    if (choice == "choice1"):
        selected_account_type = "savings"
    else:
        selected_account_type = "current"

    while (selected_account_type != actual_account_type):
        choice = getConfirmation("retry-account-type")
        if (choice == "choice1"):
            selected_account_type = "savings"
        else:
            selected_account_type = "current"

def runActions(authResult):

    ac_no, name, account_type = getAccountDetails(authResult)
    data = pd.read_csv('atmData.csv')
    person = data[data['ac'] == ac_no]

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

            logTransaction("withdraw", name, str(ac_no), str(amount))
            runCATM("Successfully withdrawn", authResult)
        else:
            runCATM("Transaction cancelled", authResult)


    elif (action == "balance"):
        balance = person['balance']
        runCATM("Your balance is: " + str(int(balance)), authResult)
        # print(balance)

    elif (action == "transfer"):

        data = pd.read_csv('atmData.csv')
        rec_ac_no = getNumber("Enter A/C no of recipient")
        recipient = data[data['ac'] == int(rec_ac_no)]

        while (len(recipient) == 0 or len(rec_ac_no) < 6):
            rec_ac_no = getNumber("Invalid recipient, try again.")
            recipient = data[data['ac'] == int(rec_ac_no)]

        while (int(rec_ac_no) == ac_no):
            rec_ac_no = getNumber("Can't transfer to own account")
            recipient = data[data['ac'] == int(rec_ac_no)]

        currUserBalance = int(person['balance'])

        amount = int(getNumber("Enter amount to transfer"))
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
            data.loc[data['ac'] == int(rec_ac_no), 'balance'] = recipientBalance
            data.to_csv('atmData.csv', index=False)

            logTransaction("transfer", name, str(ac_no), str(amount), recipientName, rec_ac_no)
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
            showInstructions(50)
        else:
            loggedIn = True

        entryPageInput = getHomepageKey(message, loggedIn, fontSize)

        if(entryPageInput == "exit"):
            exit(0)

        elif (entryPageInput == "enter"):
            if(accountNo != ""):
                runActions(accountNo)

            authResult = authenticate()
            ac_no, name, actual_account_type = getAccountDetails(authResult)
            selectAccountType(actual_account_type)
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

