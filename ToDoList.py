from enum import Enum

userInput = 0
print("==== To-Do List =====")
print("1. Add Task")
print("2. View Tasks")
print("3. Modify Task")
print("4. Remove Task")
print("5. Exit")

userInput = 0
tasks = {}

class taskStatus(Enum):
    ToDo = 1
    InProgress = 2
    Done = 3

while(userInput != 5):
    userInput = int(input("Choose a task option: "))
    if(userInput == 1):
        taskName = input("Enter name of task: ")
        tasks[taskName] = taskStatus.ToDo
    elif(userInput == 2):
        for task in tasks:
            print(f"Task: {task} - {tasks[task].name}")
    elif(userInput == 3):
        print("===== Available Status Values =====")
        print("ToDo: 1")
        print("InProgress: 2")
        print("Done: 3")
        taskName = input("Enter name of task to change status: ")
        newStatus = int(input("Enter new status(1/2/3): "))

        tasks[taskName] = taskStatus(newStatus)
        
    elif(userInput == 4):
        taskName = input("Enter name of task to delete: ")
        del tasks[taskName]
    else:
        userInput = 5