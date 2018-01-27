from googleSheetAPI import retrieveSpreadsheetData, CLIENT_SECRET_FILE
## A library of python functions to manage tasks for use of ULAB

# Function to retrieve a spreadsheet
# retrieveSpreadsheetData("1Lz50t87PPdlXymskt1uNEHd8pP7y9h9Te7i9XJCGfSg", 'A2:M', CLIENT_SECRET_FILE)
# NEED TO CHANGE SCOPES FROM READ ONLY TO READ AND WRITE

## Create and Add New Task to Google Sheet
## Return Task ID
def createTask(name, assignee, deadline, created, taskType, status, priority):
    return

## Get Task given its ID
def getTask(id):
    return

## Set Task to Completed
def completeTask(id):
    return

## Set Task to In Progress
def acceptTask(id):
    return

## Get All Tasks for a Person
def getTasksForName(name):
    return

## Return list of all Tasks
def getAllTasks():
    return

## Return list of uncompleted Tasks
def getAllUncompletedTasks():
    return