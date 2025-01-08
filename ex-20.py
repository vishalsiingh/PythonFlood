# Check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example: Check if 29 is prime
print("Prime" if is_prime(29) else "Not Prime")