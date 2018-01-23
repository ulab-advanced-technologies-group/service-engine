# Service Engine Project

## Summary
To assist or automate tasks requested by ULAB members.

## Features
* Detect when a task is submitted to the ULAB Tasking Google form.
* Parse the response data from the form and pass it into a handling function that will determine what to do for the task and execute the appropriate function(s).
* Ability to add specific handling functions for a given task in a modular fashion.
* Access the Google API and any other APIs as necessary for its functions.
* Ability to check (edit?) status of tasks.
* Generic functions for common actions such as emailing a group of people and sending periodic reminders.

## How to start the engine?
1. Read the `README.md` within the 'secrets' folder and insert necessary files.
2. Enter in the following terminal command: `pip3 install -r requirements.txt`
3. Make the 'api' folder your working directory
4. Type in the following terminal command: `python3 googleSheetAPI.py`

## General Process of Task Handling at First Submission
1. Google form has a script and an associated installable trigger that calls the function onFormSubmit when a user submits a form.
2. The function gets the form response data and the email of the user and sends it to the ULAB website in the form of a HTTP POST request.
3. The request contains a JSON payload with the data, which is received by the website.
4. Website has a general handler function which does several actions using the data:
    a. Creates task in the database which can then be later displayed to users.
    b. Runs appropriate task function for the data -- this handles the "task." (task functions come from the "service-handlers" library)
5. For multi-step tasks, runs additional handling code as necessary (for example, wait for approval).
6. Update task status and either go to next step of task (return to step 5) or completes task with final status (e.g. "completed," "failed," etc.)

## Organizational Structure of Repository
* "api" folder
    * Made into a library
* "secret" folder
    * Made into a library
* `main.py` file
* "service-providers" folder
    * Made into a library

## Task 1: Onboarding Assisting
* Use various API to assist onboarding
* Update the Status Web Page for relevant statuses

## Task 2: Room Scheduling/Booking Automation
Use Google Calendar API automate room scheduling

## Task 3: Web Application for Statuses
### Features
* Match ULAB website's web design
* Public status page
    * Search feature

* MySQL database for statuses
* Retrieve statuses from the Google sheet

### Python Class Objects
#### Class Task
* Methods
    * update_status(status)
* Properties
    * id
    * name
    * assignee
    * deadline
    * created
    * type
    * status

#### Class Tasklist
* Methods
    * add_task(task)
* Properties
    * type
    * list


## Task 4: Organize `main.py` file
Organize and document the Python file for service providers to use easily.


## Task 5: Stabilize infrastructure

### Google App Script
* Detects task submission
* Submit task data to the website through HTTP POST request
### Status Web Page
* Updates UI to relevant statuses of each individual task

### Service Engine
* Series of "if" statements to handle task
* Imports task handling methods from the "service_provider" library
* Email task assignee to be notified 
