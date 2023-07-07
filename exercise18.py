# Program that asks the user for a number and uses a loop to calculate its factorial

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num):
    fact *= i

print(f"The factorial of {num} is: {fact}")