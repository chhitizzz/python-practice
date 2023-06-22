# Program to calculate area of triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Semi-Perimeter 
s = (a + b + c) / 2 

# Area of triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print(f"The area of the triangle is {area}")