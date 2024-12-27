while True:
    print("\nSimple Calculator")
    print("1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit")
    choice = input("Choose an option: ")

    if choice == "5":
        print("Goodbye!")
        break
    elif choice in {"1", "2", "3", "4"}:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == "1":
            print(f"Result: {a + b}")
        elif choice == "2":
            print(f"Result: {a - b}")
        elif choice == "3":
            print(f"Result: {a * b}")
        elif choice == "4":
            print(f"Result: {a / b if b != 0 else 'Error (division by zero)'}")
    else:
        print("Invalid choice!")
