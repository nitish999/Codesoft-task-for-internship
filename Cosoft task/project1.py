# TO_DO_list

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Quit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def delete_task(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        try:
            view_tasks(tasks)
            task_number = int(input("\nEnter the number of the task you want to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"'{removed_task}' has been deleted from your to-do list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
