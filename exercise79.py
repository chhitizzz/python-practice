# Recursive function to calculate the factorial of a given number

def factorial(n):
    if n == 0:
        return 1 
    
    else: 
        return n * factorial(n - 1)