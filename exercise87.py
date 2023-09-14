# Program to check if an element exists in a set

numbers = {10, 20, 30, 40, 50}

element_to_check = int(input("Enter the element to check in the set: "))

if element_to_check in numbers:
    print(f"{element_to_check} exists in the set.")

else:
    print(f"{element_to_check} doesn't exist in the set.")