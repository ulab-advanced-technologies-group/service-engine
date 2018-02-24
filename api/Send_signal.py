from googleSheetAPI import retrieveSpreadsheetData, CLIENT_SECRET_FILE
from threading import Timer
from gmailAPI import send_email
from Emails import emails
import gmailAPI
credentials = gmailAPI.get_credentials()

remindDict = {"type of task": "How Often"}
actionsDict = {"type of task": "Function"}
prev_length = len(retrieveSpreadsheetData("1Lz50t87PPdlXymskt1uNEHd8pP7y9h9Te7i9XJCGfSg", 'A2:DD', CLIENT_SECRET_FILE)) #keeps track of the length

def check_and_send():
    print("Checking..")
    global prev_length
    values = retrieveSpreadsheetData("1Lz50t87PPdlXymskt1uNEHd8pP7y9h9Te7i9XJCGfSg", 'A2:DD', CLIENT_SECRET_FILE)
    if len(values) != prev_length:
        print("Found new entries. Processing...")
        new_entries = values[prev_length:]
        prev_length = len(values)
        for row in new_entries:
            send_message(row)
        print(str(len(new_entries)) + " New Entries Processed.")
    Timer(10.0, check_and_send).start() #Ask Amit, again

def send_message(row):
     message = message_handler(row)
     for person in message[0]:
        #Email for the assigned
        send_email("neeull2@gmail.com", person, message[1], message[2])
     #send_email("neeull2@berkeley.edu", "ntoledo@berkeley.edu", message[1], message[2])
     #Email for requester
     send_email("neeull2@berkeley.edu", row[8], message[3], message[4])


#Takes in request row, and returns [recipients, subject1, message1, subject2, message2]
#subject2 and message2 are for the requester
def message_handler(row):
    """Remember to implement the remind function in all cases"""
    topic = row[2]
    #actionsDict[topic]()
    row = row + ["" for x in range(99)]
    if topic == "Contacting someone from outside of ULAB":
        recipients = get_recipients(topic)
        subject = "You have been assigned a task with {} priority".format(row[3])
        message = "{} wants you to contact {} from outside of ULAB with {} priority.\nExtra Information: {}\n".format(row[9], row[27], row[3], row[28])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]
    if topic == "Getting equipment":
        recipients = get_recipients(topic)
        subject = "{} wants {} with {} priority".format(row[9], row[29], row[3])
        message = "{} wants {}. Reference: {}, Est. Cost {}, Intended use {}".format(row[9], row[29], row[30],row[31], row[32])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]
    if topic == "Getting information on a specific lab":
        recipients = get_recipients(topic)
        subject = "{} wants information from {} with {} priority".format(row[9], row[27], row[3])
        message = "{} wants information from {}.\n Note that {}".format(row[9], row[27], row[28])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]
    if topic == "Recruiting":
        recipients = get_recipients(topic)
        subject = "{} wants a new {} with {} priority".format(row[9], row[24], row[3])
        message = "{} wants a new {}.\nWork will involve {} and its requirements are {}".format(row[9], row[26], row[25])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]
    if topic == "Publicizing something":
        return
    if topic == "Reimbursement":
        return
    if topic == "Booking a room":
        return
    if topic == "Training for lab equipment":
        return
    if topic == "Attaining certification status":
        return
    if topic == "Expert Consulting":
        return
    if topic == "Activity Development":
        return
    if topic == "Securing Lab tours":
        ##form not finished
        return

    if topic == "Curricular Development":
        return
        "This is actually a work-in-progress on the Google Forms"

    if topic == "Liaison Training":
        recipients = get_recipients(topic)
        subject = "{} requests Liaison Training with {} priority".format(row[9], row[3])
        message = "{} from the {} request(s) training for {} with {} priority. Their email is {}.".format(row[9], row[10], row[33], row[3], row[35])
        hvsubject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]

    if topic == "Make a change to the website":
        recipients = get_recipients(topic)
        subject = "{} requests a change to the website with {} priority".format(row[9], row[3])
        message = "{} from the {} requests (a/an) {} kind of change for the website. \nDescription of change: {} \nReasons for the change: {} \nOptional sketch for a design change: {}".format(row[9], row[10], row[50], row[52], row[51], row[53])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]

    if topic == "On Boarding":
        recipients = get_recipients(topic)
        subject = "{} needs {} to be On-Boarded with {} priority".format(row[9], row[64], row[3])
        message = "{} from the {} needs {} to be On-Boarded with {} priority.".format(row[9], row[10], row[64], row[3])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]

    if topic == "Graphic Design":
        recipients = get_recipients(topic)
        subject = "{} has a Graphic Design request with {} priority".format(row[9], row[3])
        message = "{} from the {} needs a {} with {} priority. \nThey need this by {}. Estimated time the project will take: {}. \nExtra Information: Theme: {}. Preferred Colors: {}. Inspirational Samples: {}. Additional Comments: {}.".format(row[9], row[10], row[15], row[3], row[16], row[6], row[17], row[18], row[19], row[20])
        subject2 = "You have requested a task with {} priority".format(row[3])
        message2 = "Task for '{}' has been assigned with {} priority.".format(row[2], row[3])
        return [recipients, subject, message, subject2, message2]

    #Other Case
    print("did not find topic")
    return

def remind(row):
    print("Reminding...")
    when_remind = remindDict[row[2]]
    if (not when_remind) or (row[1] == "Yes"):
        return
    send_message(row)
    Timer(when_remind, remind, row).start()
    
def get_recipients(topic):
    return ['ntoledo@berkeley.edu']

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
