# Program to remove an element from a list

randomList = [10, 20, 30, 40, 50]

print(f"List before removing: {randomList}")

removeElement = int(input("Enter the element to remove from the list: "))

randomList.remove(removeElement);

print(f"Updated list: {randomList}")