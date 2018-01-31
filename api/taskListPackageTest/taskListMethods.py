from __future__ import print_function
from googleapiclient import discovery
from googleSheetAPI import retrieveSpreadsheetData, CLIENT_SECRET_FILE
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'ULAB TASK LIST MANAGER'
spreadsheet_id = '1Lz50t87PPdlXymskt1uNEHd8pP7y9h9Te7i9XJCGfSg'
SHEETID = 1624733238
SHEETNAME = "Automated-Service-Engine"

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'service-engine-test.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

# Update value at given Cell (A1 Format)
# Example: updateCellRequest("x", A2)
def updateCellRequest(text, cell):
    reqBody = {}
    reqBody["values"] = [[text]]
    reqBody["majorDimension"] = "COLUMNS"
    request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, valueInputOption="USER_ENTERED", range=cell, body=reqBody)
    return request.execute()

## Create and Add New Task to Google Sheets
## Return Task ID (also same as row)
## TODO: -id is unneccessary since we're using the row number anyway?
##       -also still need the date created
def createTask(name, assignee, deadline, taskType, priority, info=None, file=None):
    reqBody = {}
    reqBody["values"] = [[name, assignee, deadline, "", taskType, "Pending", info, file, priority]]
    reqBody["majorDimension"] = "ROWS"
    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, valueInputOption="USER_ENTERED", range="{}!A3".format(SHEETNAME), insertDataOption="INSERT_ROWS", body=reqBody)
    return int(request.execute()['updates']['updatedRange'].split(":")[-1][1:])

## Get Task given its ID
def getTask(id):
    return

## Set Task to Completed
def completeTask(id):
    cell = "F" + str(id)
    return updateCellRequest("Resolved", cell)

## Set Task to In Progress
def acceptTask(id):
    cell = "F" + str(id)
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

credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                'version=v4')
service = discovery.build('sheets', 'v4', http=http,
                          discoveryServiceUrl=discoveryUrl)
