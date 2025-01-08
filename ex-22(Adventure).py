def start_adventure():
    print("Welcome to the Adventure Game!")
    print("You find yourself at the entrance of a dark forest.")
    print("There are three paths ahead of you:")
    print("1. Take the left path.")
    print("2. Take the middle path.")
    print("3. Take the right path.")
    
    choice = input("Choose your path (1, 2, or 3): ")
    
    if choice == "1":
        left_path()
    elif choice == "2":
        middle_path()
    elif choice == "3":
        right_path()
    else:
        print("Invalid choice. Please try again.")
        start_adventure()

def left_path():
    print("\nYou chose the left path and encounter a hungry wolf!")
    print("What will you do?")
    print("1. Fight the wolf.")
    print("2. Run away.")
    action = input("Choose your action (1 or 2): ")
    
    if action == "1":
        print("You bravely fight the wolf and emerge victorious!")
        print("Congratulations, you survived the adventure!")
    elif action == "2":
        print("You run away safely but miss out on the treasure hidden ahead.")
    else:
        print("Invalid choice. The wolf attacks you. Game over.")
        
def middle_path():
    print("\nYou chose the middle path and find a treasure chest.")
    print("It's locked. You see a note with a riddle:")
    print("What has keys but can't open locks?")
    answer = input("Your answer: ").strip().lower()
    
    if answer == "piano":
        print("Correct! The chest opens, revealing gold and jewels!")
        print("Congratulations, you're rich!")
    else:
        print("Wrong answer. The chest remains locked forever. Game over.")

def right_path():
    print("\nYou chose the right path and fall into a hidden trap.")
    print("Unfortunately, you couldn't escape. Game over.")

# Start the game
start_adventure()
