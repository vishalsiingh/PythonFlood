tasks = []

while (choice := input("\n1. View  2. Add  3. Remove  4. Exit: ")) != "4":
    if choice == "1":
        print(*[f"{i+1}. {t}" for i, t in enumerate(tasks)] or ["No tasks"], sep="\n")
    elif choice == "2":
        tasks.append(input("New task: "))
    elif choice == "3":
        tasks.pop(int(input("Task # to remove: ")) - 1)
    else:
        print("Invalid choice!")
print("Goodbye!")
