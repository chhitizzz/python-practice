# Function that takes two numbers as arguments and returns their sum

def calculateSum(x, y):
    sum = x + y
    return sum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calculateSum(num1, num2)
print(f"The sum of {num1} and {num2} is {result}.")