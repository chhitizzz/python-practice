# Program that asks the user to enter a string and uses a loop to count the number of characters in the string

str = input("Enter a string: ")
count = 0

for char in str:
    count += 1

print(f"The number of characters in {str} is: {count}")