# Program to swap two variables 

#! Solution 1: Using third variable

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

temp = x 
x = y
y = temp

print(f"The value of x is {x}")
print(f"The value of y is {y}")

print("")

#! Solution 2: Without using third variable 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print(f"The value of x is {x}")
print(f"The value of y is {y}")