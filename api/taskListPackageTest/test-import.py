import taskListMethods as taskList
taskList.get_credentials()
taskList.createTask("neil","neil","today","equipment","urgent")
newId = taskList.createTask("phat","phat","today","contacting people","not urgent")
print(newId)
taskList.completeTask(newId)
print(taskList.numTasks())
