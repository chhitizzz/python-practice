# Program to display the multiplication table 

#! Method 1: Using for loop 

num = int(input("Enter a number: "))

for i in range (1, 11):
    print(f"{num} x {i} = {num * i}")

print("")

#! Method 2: Using while loop 