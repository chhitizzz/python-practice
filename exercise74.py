# Function that takes a list of numbers as an argument and returns the minimum and maximum values as a tuple

def findMinMax(numbers):
    if not numbers: 
        return None

    min_value = min(numbers)
    max_value = max(numbers)

    return(min_value, max_value)

num_count = int(input("Enter the number of elements: "))
num_list = []

for i in range(num_count):
    num = float(input(f"Enter number {i + 1}: "))
    num_list.append(num)