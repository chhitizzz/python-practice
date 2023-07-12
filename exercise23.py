# Program to display the multiplication table 

#! Method 1: Using for loop 

num = int(input("Enter a number: "))

print(f"The multiplication table of {num} is: ")

for i in range (1, 11):
    print(f"{num} x {i} = {num * i}")

print("")

#! Method 2: Using while loop 

number = int(input("Enter a number: "))
j = 1

print(f"The multiplication table of {number} is: ")

while j <= 10:
    print(f"{number} x {j} = {number * j}")
    j += 1