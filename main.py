import json

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def read_json(filename='tasks.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def append_to_json(new_data, filename='tasks.json'):
    data = read_json(filename)
    data['tasks'].append(new_data)

    # Write back to the file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def add_task():
    new_task = {}
    task_name = input("Name of task: ")
    due_date = input("Due date: ")

    while (1):
        priority = input("Priority (1 for low, 2 for medium, 3 for high): ")
        if ((priority == "1") | (priority == "2") | (priority == "3")):
            break
        else:
            print("You must enter 1, 2, or 3 for priority. Try again.")

    new_task["task_name"] = task_name
    new_task["due_date"] = due_date
    new_task["priority"] = priority
    new_task["completed"] = False

    append_to_json(new_task)

    print("Successfully added task. Run another command or 'quit' to quit.")

def delete_task(filename='tasks.json'):
    task_delete_name = input("Name of task you want to delete: ")
    data = read_json(filename)

    data['tasks'] = [
        task for task in data['tasks'] 
        if task.get('task_name') != task_delete_name
    ]

    newData = read_json(filename)

    if (data == newData):
        print("That task wasn't in your task list. Run the command again (or any other command).")
    
    else:
        with open('tasks.json', 'w') as file:
            json.dump(data, file, indent=4)
        print("Successfully deleted. Run the command again (or any other command).")

def list_tasks(filename='tasks.json'):
    data = read_json(filename)
    print("\nCompleted tasks appear in green. Tasks that incomplete appear in red.")
    for task in data['tasks']:

        if (task['completed']):
            completedStatus = GREEN
        else:
            completedStatus = RED

        print(f"{completedStatus}\nTask Name: {task['task_name']}\nDue Data: {task['due_date']}\nPriority: {task['priority']}\nCompleted: {task['completed']}{RESET}\n")
    
    print("Done listing tasks. Run another command.")

def complete_task(filename='tasks.json'):
    data = read_json(filename)
    foundFlag = False
    task_completed = input("Enter the name of the task to mark as completed: ")
    for task in data['tasks']:
        if task.get('task_name') == task_completed:
            if (task.get('completed') == True):
                print("This task is already complete! Run a new command.")
                return
            task['completed'] = True
            foundFlag = True
            break
    if (foundFlag == False):
        print("That task was not found. Try running the command again or running a different command.")
    else:
        with open('tasks.json', 'w') as file:
            json.dump(data, file, indent=4)
        print("Successfully updated the task to complete.")

def incomplete_task(filename='tasks.json'):
    data = read_json(filename)
    foundFlag = False
    task_completed = input("Enter the name of the task to mark as incomplete: ")
    for task in data['tasks']:
        if task.get('task_name') == task_completed:
            if (task.get('completed') == False):
                print("This task is already marked as incomplete! Run a new command.")
                return
            task['completed'] = False
            foundFlag = True
            break
    if (foundFlag == False):
        print("That task was not found. Try running the command again or running a different command.")
    else:
        with open('tasks.json', 'w') as file:
            json.dump(data, file, indent=4)
        print("Successfully updated the task to incomplete.")

def help_menu():
    print("COMMAND: 'edit', FUNCTION: Edit an entry in a task.\nCOMMAND: 'complete', FUNCTION: Marks a task as completed.\nCOMMAND: 'incomplete', FUNCTION: Marks a task as not complete.\nCOMMAND: 'add', FUNCTION: Adds a task. Will be prompted for details after running the command.\nCOMMAND: 'delete', FUNCTION: Deletes a task. Will be prompted for details after running the command.\nCOMMAND: 'list', FUNCTION: Lists all tasks on your task list.\nCOMMAND: 'help', FUNCTION: Prompts for a help menu.\nCOMMAND: 'quit', FUNCTION: Exits the program.")

def edit_task(filename='tasks.json'):
    data = read_json(filename)
    task_changed = input("Enter the task name to change: ")
    field_changed = input("Enter the exact field to change: ")

    if (field_changed == "task_name"):
        for task in data['tasks']:
            if (task.get('task_name') == task_changed):
                task[field_changed] = input("Enter new task name: ")
                print("Name changed successfully.")

    elif (field_changed == "due_date"):
        for task in data['tasks']:
            if (task.get('task_name') == task_changed):
                task[field_changed] = input("Enter a new due date: ")
                print("Due date changed successfully.")

    elif (field_changed == "priority"):
        for task in data['tasks']:
            if (task.get('task_name') == task_changed):
                new_priority = input("Enter a new priority: ")
                if ((new_priority == "1") | (new_priority == "2") | (new_priority == "3")):
                    task[field_changed] = new_priority
                    print("Priority changed successfully.")
                else:
                    print("That priority is invalid. Please enter a value between 1-3. Run the command again.")

    elif (field_changed == "completed"):
        print("Use 'complete' or 'incomplete' commands to change this field.")

    else:
        print("That field was not found. Run the command again.")
        
    with open('tasks.json', 'w') as file:
        json.dump(data, file, indent=4)

def filter_tasks(filename='tasks.json'):
    data = read_json(filename)
    filterParam = input("Enter the field name you'd like to filter by: ")
    filterValue = input("Enter the value you'd like to see: ")

    if (filterParam == 'completed'):
        if filterValue.lower() == "true":
            filterValue = True
        else:
            filterValue = False

    for task in data['tasks']:
        if (task['completed'] == True):
            completedStatus = GREEN
        else:
            completedStatus = RED
        if (task.get(filterParam) == filterValue):
            print(f"{completedStatus}\nTask Name: {task['task_name']}\nDue Data: {task['due_date']}\nPriority: {task['priority']}\nCompleted: {task['completed']}\n{RESET}")

    print("Finished displaying.")

def main():
    print("Hello! Welcome to ClickTask! What would you like to do? (run help for help)")
    while (1):
        modeSelect = input("")
        if (modeSelect == "help"):
            help_menu()

        elif (modeSelect.lower() == "filter"):
            filter_tasks()
        
        elif (modeSelect.lower() == "add"):
            add_task()

        elif (modeSelect.lower() == "edit"):
            edit_task()
        
        elif (modeSelect.lower() == "delete"):
            delete_task()

        elif (modeSelect.lower() == "list"):
            list_tasks()

        elif (modeSelect.lower() == "complete"):
            complete_task()

        elif (modeSelect.lower() == "incomplete"):
            incomplete_task()

        elif (modeSelect.lower() == "quit"):
            quit()

        else:
            print("That command was not found. Try again or use 'help' command.")

main()