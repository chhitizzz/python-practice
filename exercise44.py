# Program to access the nth element of a list

randomList = [10, 20, 30, 40, 50]

n = int(input("Enter the index of the element to access starting from 0: "))

if 0 <= n < len(randomList):
    element = randomList[n]
    print(f"The element at index {n} is: {element}")

else: 
    print("Invalid index. The list doesn't have an element at that index.")