# Program to check if an element exists in a tuple

myTuple = (10, 20, 30, 40, 50, 60)

print("The tuple is:", myTuple)

elementToCheck = int(input("Enter the element to check: "))

if elementToCheck in myTuple:
    print(f"The element {elementToCheck} is in the tuple.")

else:
    print(f"The element {elementToCheck} is not in the tuple.")