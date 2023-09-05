# Recursive function to calculate the nth Fibonacci number.

def fibonacci_sequence(n):
    if n <= 0:
        return 0
    
    elif n == 1:
        return 1

    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)
    
n = int(input("Enter the value of n to calculate the nth Fibonacci number: "))

result = fibonacci_sequence(n)
print(f"The {n}th Fibonacci number is {result}")