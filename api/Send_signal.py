from googleSheetAPI import retrieveSpreadsheetData, CLIENT_SECRET_FILE
from threading import Timer

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
            to = row[4]
            send_message(message, to)
        return Timer(5.0, check_and_send).start()



def send_message(message, to):
    print(message)
    print(to)
    #return #send a get request to our website

check_and_send() #runs for the first time immediately
