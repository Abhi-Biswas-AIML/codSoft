tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")


def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        print(f"Task at index {index} deleted.")
    else:
        print("Invalid index.")

def update_task(index):
    if 0 <= index < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[index] = new_task
        print("Task updated successfully.")
    else:
        print("Invalid index.")


while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. EXIT")



    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        index = int(input("Enter the index of the task to delete: "))
        delete_task(index-1)
    elif choice == '4':
        index = int(input("Enter the index of the task to update: "))
        update_task(index-1)
    elif choice == '5':
        break
    else:
        print("Invalid Option !!!!!")
    