# Function that takes a number as an argument and returns "Even" if the number is even, and "Odd" if it's odd

def checkNumber(number):
    if (number % 2 == 0):
        return 'Even'
    
    else:
        return 'Odd'

num = int(input("Enter a number: "))

result = checkNumber(num)
print(f"The number {num} is {result}.") 