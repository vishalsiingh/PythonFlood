# Program to calculate the average of numbers

# Function to calculate the average
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Main code
try:
    # Input: List of numbers from the user
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(float, user_input.split()))
    
    # Calculate the average
    average = calculate_average(numbers)
    print("The average of the numbers is:", average)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
