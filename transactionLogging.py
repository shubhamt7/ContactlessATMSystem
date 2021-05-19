from screenshot import getCurrentDateAndTime
import os.path as path
from pathlib import Path

def logTransaction(type, currentUserName = "", curr_ac_no = "", amount = "", recipientName = "", recipient_ac_no = ""):

    #Computing the file name based on current date
    currentDate, currentTime = getCurrentDateAndTime()
    fileName = str(currentDate) + ".txt"
    filePath = path.join(Path.cwd(), "transactions", fileName)

    # Transaction message if the user performed transfer
    if type == "transfer":
        transactionDetails = currentUserName + " (" + curr_ac_no + ") transferred Rs. " + amount + " to " + recipientName \
                             + " (" + recipient_ac_no + ") at " + str(currentTime)

    # Transaction message if the user performed withdrawal
    else:
        transactionDetails = currentUserName + " (" + curr_ac_no + ") withdrew Rs. " + amount + " at " + str(currentTime)

    #Writing the transaction entry to file
    with open(filePath, "a+") as f:
        f.seek(0)
        data = f.read(100)
        if len(data) > 0:
            f.write("\n")
        f.write(transactionDetails)