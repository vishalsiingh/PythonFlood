# Fibonacci sequence up to n
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b

# Example: Print Fibonacci numbers up to 100
fibonacci(100)
