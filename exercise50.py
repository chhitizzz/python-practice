# Program to check if a given element exists in a list

myList = [10, 20, 30, 40, 50, 60]

print("List: ", myList)

elementExists = int(input("Enter the element to check in the list: "))

if elementExists in myList:
    print("The element exists in the list.")

else: 
    print("The element doesn't exist in the list.")