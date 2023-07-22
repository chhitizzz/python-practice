# Program to count the occurrences of a specific character in a string

user_input = input("Enter a string: ")
characters_to_count = input("Enter the character to count: ")

count = 0

for char in user_input:
    if char == characters_to_count:
        count += 1

print(f"The character '{characters_to_count}' appears {count} times in {user_input}.")