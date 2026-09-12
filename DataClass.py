from dataclasses import dataclass

@dataclass
class DataClass:
    taskName: str
    priority: int
    completed: bool

taskName = input("Enter the task name: ")
priority = int(input("Enter the priority (1-5): "))
completed = input("Is the task completed? (yes/no): ").strip().lower() == "yes"

task = DataClass(taskName, priority, completed)

print(f"Task Name: {task.taskName}")
print(f"Priority: {task.priority}")
if task.completed:
    print("Status: Completed")
else:
    print("Status: Not Completed")