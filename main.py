import cv2
import pandas as pd
from keyboardNumpad import getNumber
from keyboardHomepage import getHomepageKey
from keyboardConfirmation import getConfirmation
from keyboardActionChoice import getAction
from authenticate import authenticate
from instructionsPage import showInstructions
from transactionLogging import logTransaction
from utility import CameraUtility

def getAccountDetails(account_no):
    ac_no = int(str(account_no))
    data = pd.read_csv('atmData.csv')
    person = data[data['ac'] == ac_no]
    name = str(person['name'].values[0])
    account_type = str(person['account_type'].values[0])

    return ac_no, name, account_type

def selectAccountType(language, actual_account_type):
    choice = getConfirmation(language, "account-type")
    if (choice == "choice1"):
        selected_account_type = "savings"
    else:
        selected_account_type = "current"

    while (selected_account_type != actual_account_type):
        choice = getConfirmation(language, "retry-account-type")
        if (choice == "choice1"):
            selected_account_type = "savings"
        else:
            selected_account_type = "current"

def runActions(language, authResult):

    ac_no, name, account_type = getAccountDetails(authResult)
    data = pd.read_csv('atmData.csv')
    person = data[data['ac'] == ac_no]

    action = getAction(language)
    actionConfirmation = getConfirmation(language, action + "-action")

    while (actionConfirmation != "choice1"):
        action = getAction(language)
        actionConfirmation = getConfirmation(language, action + "-action")


    print(action)

    if (action == "withdraw"):
        amount = int(getNumber(language, "enter-amount"))
        balance = int(person['balance'])

        while (amount > balance):
            amount = int(getNumber(language, "not-enough-balance"))

        while (amount == 0):
            amount = int(getNumber(language, "zero-amount"))

        while(amount < 100 or amount % 100 != 0):
            amount = int(getNumber(language, "invalid-denomination"))

        confirmationMessage = getConfirmation(language, "withdraw", name, amount, balance)
        print(confirmationMessage)

        if (confirmationMessage == "choice1"):
            newBalance = balance - amount
            data.loc[data['ac'] == ac_no, 'balance'] = newBalance
            data.to_csv('atmData.csv', index=False)
            logTransaction("withdraw", name, str(ac_no), str(amount))
            runCATM("withdraw-success", authResult, language = language)
        else:
            runCATM("cancelled-txn", authResult, language = language)


    elif (action == "balance"):
        balance = person['balance']
        if(language == "hindi"):
            message = "प्रिय ग्राहक, आपके बैलेंस में " + str(int(balance)) + " रुपये बचे हैं"
        else:
            message = "Dear customer,your balance is Rs." + str(int(balance))

        runCATM(message, authResult, language = language)
        # print(balance)

    elif (action == "transfer"):

        data = pd.read_csv('atmData.csv')
        rec_ac_no = getNumber(language, "enter-recipient")
        recipient = data[data['ac'] == int(rec_ac_no)]

        while (len(recipient) == 0 or len(rec_ac_no) < 6):
            rec_ac_no = getNumber(language, "invalid-recipient")
            recipient = data[data['ac'] == int(rec_ac_no)]

        while (int(rec_ac_no) == ac_no):
            rec_ac_no = getNumber(language, "self-transfer")
            recipient = data[data['ac'] == int(rec_ac_no)]

        currUserBalance = int(person['balance'])

        amount = int(getNumber(language, "enter-amount"))
        while (amount > currUserBalance):
            amount = int(getNumber(language, "not-enough-money"))

        while (amount == 0):
            amount = int(getNumber(language, "zero-amount"))

        recipientBalance = int(recipient['balance'])
        recipientName = str(recipient['name'].values[0])

        confirmationMessage = getConfirmation(language, "transfer", name, amount, currUserBalance, rec_ac_no)

        if (confirmationMessage == "choice1"):
            currUserBalance = currUserBalance - amount
            recipientBalance = recipientBalance + amount
            data.loc[data['ac'] == ac_no, 'balance'] = currUserBalance
            data.loc[data['ac'] == int(rec_ac_no), 'balance'] = recipientBalance
            data.to_csv('atmData.csv', index=False)

            logTransaction("transfer", name, str(ac_no), str(amount), recipientName, rec_ac_no)
            runCATM("transfer-success", authResult, language = language)
        else:
            runCATM("cancelled-txn", authResult, language = language)

    elif action == "cancel":
        runCATM("cancelled-txn", authResult, language = language)


def runCATM(message="", accountNo = "", fontSize = 1.2, language = ""):
    try:

        cap = CameraUtility.getInstance()
        cap.read()
        cv2.namedWindow('Contactless ATM System', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Contactless ATM System', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        if(accountNo == ""):
            loggedIn = False

            canContinue = showInstructions(1)
            if canContinue == False:
                cap.release()
                cv2.destroyAllWindows()
                return

            languageInput = getConfirmation("", "language")

            if(languageInput == "choice1"):
                language = "english"
            elif(languageInput == "choice2"):
                language = "hindi"
            else:
                exit(0)

            print(language)

        else:
            loggedIn = True

        entryPageInput = getHomepageKey(language, message, loggedIn, fontSize)

        if(entryPageInput == "exit"):
            exit(0)

        elif (entryPageInput == "enter"):
            if(accountNo != ""):
                runActions(language, accountNo)

            authResult = authenticate(language)
            ac_no, name, actual_account_type = getAccountDetails(authResult)
            selectAccountType(language, actual_account_type)
            runActions(language, authResult)

    except Exception as e:
        print(e)

try:
    runCATM("welcome-message")
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

