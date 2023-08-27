# Function that calculates the factorial of a given number using recursion

def calculateFactorial(number):
    if number == 0:
        return 1 
    
    else: 
        return number * calculateFactorial(number - 1)
    
num = int(input("Enter a number: "))

result = calculateFactorial(num)
print(f"The factorial of {num} is {result}.")