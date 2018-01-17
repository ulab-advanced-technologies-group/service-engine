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


#Takes in request row, and returns [recipients, subject1, message1, subject2, message2]
#subject2 and message2 are for the requester
def message_handler(row):
    """Remember to implement the remind function in all cases"""
    topic = row[2]
    #Why are we not changing to elif?
    if topic == "Contacting someone from outside of ULAB":
        recipients = get_recipients(group)
        subject = "You have been assigned a task with {} priority".format(row[3])
        message = "{} wants you to contact {} from outside of ULAB with {} priority.\nExtra Information: {}\n".format(row[9], row[27], row[3], row[28])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]
    elif topic == "Getting equipment":
        recipients = get_recipients(group)
        subject = "{} wants {} with {} priority".format(row[9], row[29], row[3])
        message = "{} wants {}. Reference: {}, Est. Cost {}, Intended use {}".format(row[9], row[29], row[30],row[31], row[32])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]
    elif topic == "Getting information on a specific lab":
        recipients = get_recipients(group)
        subject = "{} wants information from {} with {} priority".format(row[9], row[27], row[3])
        message = "{} wants information from {}.\n Note that {}".format(row[9], row[27], row[28])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]
    elif topic == "Recruiting":
        recipients = get_recipients(group)
        subject = "{} wants a new {} with {} priority".format(row[9], row[24], row[3])
        message = "{} wants a new {}.\nWork will involve {} and its requirements are {}".format(row[9], row[26], row[25])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]
    elif topic == "Publicizing something":
        return
    elif topic == "Reimbursement":
        return
    elif topic == "Booking a room":
        return
    elif topic == "Training for lab equipment":
        return
    elif topic == "Attaining certification status":
        return
    elif topic == "Expert Consulting":
        return
    elif topic == "Activity Development":
        return
    elif topic == "Securing Lab tours":
        return
    elif topic == "Curricular Development":
        return

    elif topic == "Liaison Training":
        return

    elif topic == "Make a change to the website":
        return

    elif topic == "On Boarding":
        return

    elif topic == "Graphic Design":
        recipients = get_recipients(group)
        subject = "{} has a Graphic Design request with {} priority".format(row[9], row[3])
        message = "{} from the {} needs a {} with {} priority. \nThey need this by {}. Estimated time the project will take: {}. \nExtra Information: Theme: {}. Preferred Colors: {}. Inspirational Samples: {}. Additional Comments: {}.".format(row[9], row[10], row[15], row[3], row[16], row[6], row[17], row[18], row[19], row[20])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]
    #Other Case
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

# Contacting someone from outside of ULAB
# Getting equipment
# Getting information on a specific lab
# Recruiting
# Publicizing something
# Reimbursement
# Booking a room
# Training for lab equipment
# Attaining certification status
# Expert Consulting
# Activity Development
# Securing Lab tours
# Curricular Development
# Liaison Training
# Make a change to the website
# On Boarding
# Graphic Design
