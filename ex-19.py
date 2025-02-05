# Fibonacci sequence up to n
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b


fibonacci(100)
