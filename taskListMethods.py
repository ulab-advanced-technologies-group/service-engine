from googleapiclient import discovery
from googleSheetAPI import retrieveSpreadsheetData, CLIENT_SECRET_FILE
# ensure python client library is installed `pip install --upgrade google-api-python-client`


## A library of python functions to manage tasks for use of ULAB
credentials = 'https://www.googleapis.com/auth/spreadsheets'
service = discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id = ...

# Update value at given Cell (A1 Format)
# Example: updateCellRequest("x", A2)
def updateCellRequest(text, cell):
    reqBody = {}
    reqBody["values"] = [[text]]
    reqBody["majorDimension"] = "COLUMNS"
    reqBody["range"] = cell
    request = service.spreadsheets().values().update(spreadsheetId=spreadseet_id, body=reqBody)
    return request.execute()
    

## Create and Add New Task to Google Sheets
## Return Task ID (also same as row)
## TODO: -id is unneccessary since we're using the row number anyway?
##       -also still need the date created
def createTask(name, assignee, deadline, created, taskType, info=null, file=null, priority):
    reqBody = {}
    reqBody["values"] = [["", name, assignee, deadline, "", taskType, "", info, "", "", priority]]
    reqBody["majorDimension"] = "ROWS"
    reqBody["range"] = "A2"
    reqBody["valueInputOption"] = "USER_ENTERED"
    reqBody["insertDataOption"] = "INSERT_ROWS"
    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, body=reqBody)
    return request.execute()

## Get Task given its ID
def getTask(id):
    return

## Set Task to Completed
def completeTask(id):
    cell = "G" + str(id)
    return updateCellRequest("Resolved", cell)

## Set Task to In Progress
def acceptTask(id):
    cell = "G" + str(id)
    return updateCellRequest("In Progress", cell)

## Get All Tasks for a Person
def getTasksForName(name):
    return

## Return list of all Tasks
def getAllTasks():
    return

## Return list of uncompleted Tasks
def getAllUncompletedTasks():
    return