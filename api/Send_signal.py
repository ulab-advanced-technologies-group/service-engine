from googleSheetAPI import retrieveSpreadsheetData, CLIENT_SECRET_FILE
from threading import Timer
from gmailAPI import send_email
from Emails import emails

prev_length = -1 #keeps track of the length

def check_and_send():
    print("Checking..")
    global prev_length
    values = retrieveSpreadsheetData("1Lz50t87PPdlXymskt1uNEHd8pP7y9h9Te7i9XJCGfSg", 'A2:M', CLIENT_SECRET_FILE)
    if len(values) != prev_length:
        prev_length = len(values)
        data = filter(lambda x: x[1].lower != "yes", values) # Since I don't know how to delete rows, which would be even better.
        for row in data:
            message = "Look, you have a {} priority message from {}: {}".format(row[3], row[5], row[2])
            send_message(row[4], "You have been assigned a task", message)
            send_message(row[5], "You have just assigned {} a task".format(row[4]), "Task has been assgined")
        return Timer(1800.0, check_and_send).start() #Ask Amit, again

def send_message(to_whom, subject, message):
    email_to_send = emails[to_whom]
    send_email("phatpham@berkeley.edu", emails[to_whom], subject, message )


check_and_send() #runs for the first time immediately
