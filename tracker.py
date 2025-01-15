def display_menu():
    print("\n--- Period Tracker App ---")
    print("1. Log Last Period Date")
    print("2. View Period History")
    print("3. Calculate Next Period Date")
    print("4. Exit")

def log_period(user_data):
    date = input("Enter your last period date (YYYY-MM-DD): ")
    user_data.append(date)
    print("Period date logged successfully!")

def view_period_history(user_data):
    if not user_data:
        print("No period dates logged yet.")
    else:
        print("\nYour Period History:")
        for i, date in enumerate(user_data, start=1):
            print(f"{i}. {date}")

def calculate_next_period(user_data):
    if not user_data:
        print("No data available to calculate next period.")
        return
    
    from datetime import datetime, timedelta

    try:
        last_date = datetime.strptime(user_data[-1], "%Y-%m-%d")
        cycle_length = int(input("Enter your average cycle length (in days): "))
        next_date = last_date + timedelta(days=cycle_length)
        print(f"Your next period date is likely to be: {next_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid date format. Please log a valid date first.")

def main():
    user_data = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            log_period(user_data)
        elif choice == "2":
            view_period_history(user_data)
        elif choice == "3":
            calculate_next_period(user_data)
        elif choice == "4":
            print("Thank you for using the Period Tracker App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
