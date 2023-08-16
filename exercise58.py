# Program to count the occurrences of an element in a tuple

myTuple = (10, 20, 30, 20, 30, 10)

print("The tuple is:", myTuple)

elementToCount = int(input("Enter the element to count: "))

occurences = myTuple.count(elementToCount)

print(f"The element {elementToCount} appears {occurences} times in the tuple.")