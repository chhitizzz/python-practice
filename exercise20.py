# Program that asks the user for a number and uses a loop to print a triangle pattern of asterisks. The number of rows in the triangle should be equal to the entered number.

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    for j in range(i):
        print("*", end="")
    print()