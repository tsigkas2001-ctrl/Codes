def show_menu():
    print("--- Menu ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Delete all tasks")
    print("5. Exit")

def show_task():
    print("--- Tasks ---\n")
    try:
        with open("tasks.txt" , "r") as f:   
            lines = f.readlines()
            for line in lines:
                print("-" + line.strip())
    except FileNotFoundError:
        print("Task not found!")

def add_task():
    task = input("Add your task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task saved...")      

def task_to_delete():
    del_task = input("Enter the task you wanna delete: ")
    with open("tasks.txt" , "r") as f:
        lines = f.readlines()
    
    found = False

    with open("tasks.txt" , "w") as f:
        for line in lines:
            data = line.strip()

            if data[0].upper() == del_task.upper():
                found = True
                print(f"{data[0]} deleted!")

            else:
                f.write(line)
        
        if not found:
            print("Task not found!")

def del_all_task():
    print("Press '1' to delete all your tasks\nPress any button to return")
    del_all = input("\nAre you sure, you want to delete all your tasks? ")

    if del_all == "1":
        with open("tasks.txt", "w") as f:
            print("\nAll Tasks deleted!")

    else:
        print("\nReturning to menu...\n")
        

show_menu()

while True:
    
    choice = input("\nSelect: ")      
    
    if choice  == "1":
        show_task()
        
    elif choice == "2":
        add_task()

    elif choice == "3":
        task_to_delete()

    elif choice == "4":
        del_all_task()

    elif choice == "5":
        print("Goodbye!\n")
        break

    else:
        print("Error, Please try again!")
        continue
    