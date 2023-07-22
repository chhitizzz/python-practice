# Program to count the occurrences of a specific character in a string

user_input = input("Enter a string: ")
characters_to_count = input("Enter the number of characters to count: ")

count = 0

for char in user_input:
    if user_input == characters_to_count:
        count += 1
