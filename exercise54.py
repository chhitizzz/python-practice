# Program to access the nth element of a tuple

randomTuple = ('France', 10, 'Mbappe', 19, 'Lucario')

print("The tuple is", randomTuple)

n = int(input("Enter the index of the element to access starting from 0: "))

if 0 <= n < len(randomTuple):
    element = randomTuple[n]
    print(f"The element at index {n} is: {element}")

else: 
    print("Invalid index. The tuple doesn't have an element at that index.")