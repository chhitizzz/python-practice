# Function that calculates the factorial of a given number using recursion

def calculateFactorial(number):
    if number == 0:
        return 1 
    
    else: 
        return number * calculateFactorial(number - 1)