"""Build a simple Command Line Interface that welcomes users and displays a menu with options to add, view, delete tasks,
or quit the application. Tasks should be stored in a Python list. Use input() to capture user selections and ensure 
proper input validation to handle invalid choices. Implement error handling using try, except, else, and finally
blocks to catch errors. Alert the user if they provide invalid input, if there are no tasks to view,
if they try to delete a task that doesn't exist, and if they select an option on the menu that doesn't exist."""

tasks = []


# Show the menu options
def show_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Quit")


# Add tasks to the Python list. Alerts the user if an empty string is entered. 
def add_task(): 
    task = input("Enter your next task: ").strip()
    if task == "":
        print("Cannot enter empty task")
        return

    tasks.append(task)
    print("Task added to the list!")

# Prints the tasks list labeled with numbers. If there is nothing in the list alert the user. 
def view_tasks():
    if len(tasks) == 0:
        print("There are no tasks left.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Deletes the selected task by inputting the labeled number. Alerts the user if there are no tasks to delete or tries to delete a task that doesn't exist. 
def delete_task():

    if len(tasks) == 0:
        print("There are no tasks to delete.")
        return

    view_tasks()

    try:
        choice = int(input("Enter task number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
    else:
        if choice < 1 or choice > len(tasks):
            print("Invalid task number.")
        else: 
            removed = tasks.pop(choice - 1)
            print(f"Deleted task: {removed}")
    finally: 
        print("Returning to menu...")
    


def main():
    print("Welcome to the To-Do List App!")

    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4": 
            print("See you next time!")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()