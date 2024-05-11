taskList = []

def add_task():
    task_name = input("Input the task name: ")
    task_description = input("Describe the task: ")
    task_date_to_execute = input("Enter the date of the task: ")
    
    task = {
        "name": task_name,
        "description": task_description,
        "datee": task_date_to_execute
    }
    taskList.append(task)
    
def display_task():
    if not taskList:
        print("No tasks yet 🚫")
    else:
        print("----- Tasks -----")
        for index, task in enumerate(taskList):
            print(f"Task {index + 1}")
            print(f"Name: {task['name']}")
            print(f"Description: {task['description']}")
            print(f"Date: {task['datee']}")
            if 'done' in task:
                print("Status: Done✅")
            else:
                print("Status: Not Done☑")
            print()

def delete_task():
    if not taskList:
        print("No tasks to delete")
        return

    task_index = int(input("Enter the task number to delete: "))

    if task_index < 1 or task_index > len(taskList):
        print("Invalid task number")
        return

    deleted_task = taskList.pop(task_index - 1)
    print(f"Task '{deleted_task['name']}' deleted successfully 🚮")
    
def mark_task_done():
    if not taskList:
        print("No tasks to mark as done")
        return

    task_index = int(input("Enter the task number to mark as done: "))

    if task_index < 1 or task_index > len(taskList):
        print("Invalid task number")
        return

    task = taskList[task_index - 1]
    if 'done' in task:
        print("Task is already marked as done")
    else:
        task['done'] = True
        print(f"Task '{task['name']}' marked as done✅")

def modify_task():
    if not taskList:
        print("No tasks to modify")
        return

    task_index = int(input("Enter the task number to modify: "))

    if task_index < 1 or task_index > len(taskList):
        print("Invalid task number")
        return

    task = taskList[task_index - 1]
    print(f"Modifying Task {task_index}")
    print(f"Current Name: {task['name']}")
    print(f"Current Description: {task['description']}")
    print(f"Current Date: {task['datee']}")

    new_name = input("Enter the new name (press enter to keep current): ")
    new_description = input("Enter the new description (press enter to keep current): ")
    new_date = input("Enter the new date (press enter to keep current): ")

    if new_name:
        task['name'] = new_name
    if new_description:
        task['description'] = new_description
    if new_date:
        task['datee'] = new_date

    print(f"Task {task_index} modified successfully")    

while True:
    print("----- Task Manager -----")
    print("1. Add a task!")
    print("2. Display tasks!")
    print("3. Delete a task!")
    print("4. Mark a task as done!")
    print("5. Modify a task!")
    print("6. Quit the program")

    choice = int(input("Pick an option: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        display_task()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        mark_task_done()
    elif choice == 5:
        modify_task()
    elif choice == 6:
        break
    else:
        print("Invalid option, pick a new one")