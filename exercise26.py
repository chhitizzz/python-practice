# Program to find Armstrong Number in an interval

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))


for num in range(lower, upper + 1):
    sum = 0
    temp = num 
    while temp > 0: 
        digit = temp % 10