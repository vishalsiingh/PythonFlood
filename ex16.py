tasks = []

while True:
    print("\n1. View Tasks  2. Add Task  3. Remove Task  4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("\nTasks:", *[f"{i+1}. {t}" for i, t in enumerate(tasks)] or ["No tasks yet!"], sep="\n")
    elif choice == "2":
        tasks.append(input("Enter a task: "))
        print("Task added!")
    elif choice == "3":
        try:
            tasks.pop(int(input("Task number to remove: ")) - 1)
            print("Task removed!")
        except (ValueError, IndexError):
            print("Invalid number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
