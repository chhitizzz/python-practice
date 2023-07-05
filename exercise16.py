# Program that asks the user for a number and uses a loop to print the multiples of that number up to 10

num = int(input("Enter a number: "))

print(f"The multiples of {num} are:")

for i in range(1, 11):
    multiple = num * i
    print(multiple)