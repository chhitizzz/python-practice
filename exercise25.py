# Program to check Armstrong number

'''
Armstrong number: is a number that is the sum of its own digits each raised to the power of the number of digits. 

An example of an Armstrong number is: 
153 = (1 x 1 x 1) + (5 x 5 x 5) + (3 x 3 x 3) 
153 = 1 + 125 + 27
153 = 153
'''

num = int(input("Enter a number: "))
order = len(str(num))

sum = 0
temp = num 

while temp > 0:
    digit = temp % 10
    cube = digit ** order
    sum = sum + cube
    temp //= 10

if sum == num:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")