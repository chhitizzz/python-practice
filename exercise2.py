# Program to find square root of a number 

#! Solution 1
num1 = int(input("Enter a number: "))

sqr = num1 ** (1/2) 
print(f"The square root of {num1} is {sqr}")

print("")

#! Solution 2: Solving using Math Module 
import math

num2 = int(input("Enter a number: "))

sr = math.sqrt(num2)

print(f"The square root of {num2} is {sr}")