from screenshot import getCurrentDateAndTime
import os.path as path
from pathlib import Path

def logTransaction(type, currentUserName = "", curr_ac_no = "", amount = "", recipientName = "", recipient_ac_no = ""):

    currentDate, currentTime = getCurrentDateAndTime()
    fileName = str(currentDate) + ".txt"
    filePath = path.join(Path.cwd(), "transactions", fileName)

    #transfer
    if(type == "transfer"):
        transactionDetails = currentUserName + " (" + curr_ac_no + ") transferred Rs. " + amount + " to " + recipientName \
                             + " (" + recipient_ac_no + ") at " + str(currentTime)

    #withdraw
    else:
        transactionDetails = currentUserName + " (" + curr_ac_no + ") withdrew Rs. " + amount + " at " + str(currentTime)

    with open(filePath, "a+") as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        f.write(transactionDetails)