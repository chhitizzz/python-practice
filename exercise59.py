# Program to find the index of an element in a tuple

myTuple = (10, 20, 30, 40, 50, 60)

print("The tuple is:", myTuple)

indexOfElement = int(input("Enter the element to find in the tuple:"))

result = myTuple.index(indexOfElement)

print(result)