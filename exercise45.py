# Program to append an element to a list

randomList = [10, 20, 30, 40, 50]

element_to_append = int(input("Enter an element to append to the list: "))

print(f"List before append: {randomList}")

randomList.append(element_to_append)

print(f"Updated list: {randomList}")