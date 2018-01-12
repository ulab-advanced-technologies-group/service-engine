from googleSheetAPI import retrieveSpreadsheetData
from Thread import Timer

prev_lenth = -1 #keeps track of the lenth

def check_and_send():
    nonlocal prev_lenth
    values = retrieveSpreadsheetData("1Lz50t87PPdlXymskt1uNEHd8pP7y9h9Te7i9XJCGfSg", 'A2:M', CLIENT_SECRET_FILE)
    if len(value) != prev_lenth:
        prev_lenth = len(value)
        data = filter(value, lambda x: x[1].lower != yes) #since I don't know how to delete rows, which wh=ould be even better
        for row in data:
            message = "Look, you have a {} priority message from {}: {}".format(row[3], row[5], row[2])
            to = row[4]
            send_message(message, to)
        return Timer(1800.0, check_and_send).start()



def send_message(message, to):
    pass #send a get request to our website

check_and_send() #runs for the first time immediately
