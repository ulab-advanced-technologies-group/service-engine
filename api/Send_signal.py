from googleSheetAPI import retrieveSpreadsheetData, CLIENT_SECRET_FILE
from threading import Timer
from gmailAPI import send_email
from Emails import emails

remindDict = {"type of task": "How often"}
prev_length = len(retrieveSpreadsheetData("1Lz50t87PPdlXymskt1uNEHd8pP7y9h9Te7i9XJCGfSg", 'A2:M', CLIENT_SECRET_FILE)) #keeps track of the length

def check_and_send():
    print("Checking..")
    global prev_length
    values = retrieveSpreadsheetData("1Lz50t87PPdlXymskt1uNEHd8pP7y9h9Te7i9XJCGfSg", 'A2:M', CLIENT_SECRET_FILE)
    if len(values) != prev_length:
        new_entries = values[:prev_length]
        prev_length = len(values)
        for row in new_entries:
            send_message(row)
        Timer(10.0, check_and_send).start() #Ask Amit, again

def send_message(row):
     message = message_handler(row)
     for person in message[0]:
         #Email for the assigned
         send_email("phatpham@berkeley.edu", message[0][person], message[1], message[2])
     #Email for requester
     send_email("phatpham@berkeley.edu", row[11], message[3], message[4])


#Takes in request row, and returns [recipients, subject2, message1, subject2, message2]
def message_handler(row):
    return

def remind(row):
    print("Reminding...")
    when_remind = remindDict[row[2]]
    if (not when_remind) or (row[1] = "Yes"):
        return
    send_message(row)
    Timer(when_remind, remind, row).start()

check_and_send() #runs for the first time immediately
Timer(21600, remind).start()
