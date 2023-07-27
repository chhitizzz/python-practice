# Program to check if a given string ends with a specific suffix

user_input = input("Enter a string: ")
suffix_to_check = input("Enter a suffix to check: ")

if user_input.endswith(suffix_to_check):
    print(f"The string {user_input} ends with the suffix '{suffix_to_check}.'")