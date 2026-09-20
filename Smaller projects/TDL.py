import json

file_name = "todo_list.json"

def load_tasks():
    # This opens the file for use and loads the tasks from it. If the file doesn't exist, it creates a new one with an empty list of tasks.
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display")
    else:
        print("Your To-Do list: \n")
        for ind, task in enumerate(task_list, 1):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{ind}. {task['description']} | {status}")
        print("\n")
def mark_task_complete(tasks):
    task_list = tasks["tasks"]
    
    if len(task_list) == 0:
        print("No tasks to update.")
    else:
        try:
            which_to_update = int(input("Enter the number of the task you wish to update: ")) - 1
            task_list[which_to_update]['complete'] = True
            save_tasks(tasks)
            print("Task updated successfully.")
        except:
            print("Please enter a valid number/int")
            return   


def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file) # dump grabs the dictionary and writes it to the file in JSON format
    except:
        print("Failed to save tasks to file.")

def create_tasks(tasks):
    description = input("Enter a description for this task: ").strip()
    if description:
        #We do tasks["tasks"] since the format isn't that the dictionary iis named tasks. rather, we enter a dictionary with the value "tasks" so we must access "tasks".
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Description can't be empty")


def delete_task(tasks):
    task_list = tasks["tasks"]
    
    if len(task_list) == 0:
        print("There's no task to delete.")
    else:
        try:
            which_to_delete = int(input("Enter the number of the task you wish to delete: ")) - 1
            task_list.pop(which_to_delete)
            save_tasks(tasks)
            print("Task deleted succesfully.")
        except:
            print("Please enter a valid number/int")
            return


def display_list_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. See option menu")
    print("5. Delete a task")
    print("6. Exit")

def main():
    tasks = load_tasks()
    
    display_list_menu()
    while True:       
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            display_list_menu()
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()