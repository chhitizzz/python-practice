# Program to check if a number is positive, negative or zero

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number")

elif num == 0:
    print("Zero")

else:
    print(f"{num} is a negative number")