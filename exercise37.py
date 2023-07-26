# Program to check if a given string starts with a specific prefix.

user_input = input("Enter a string: ")
prefix_to_check = input("Enter a prefix to check: ")

if user_input.startswith(prefix_to_check):
    print(f"The string '{user_input}' starts with the prefix '{prefix_to_check}'.")

else: 
    print(f"The string '{user_input}' doesn't starts with the prefix '{prefix_to_check}'.")