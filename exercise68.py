# Function that takes a list of numbers as an argument and returns a new list containing only the positive numbers

def positiveNumbers(numbers):
    positive_numbers = []

    for num in numbers: 
        if num > 0:
            positive_numbers.append(num)
        
    return positive_numbers

num_count = int(input("Enter the number of elements: "))
num_list = []

for i in range(num_count):
    num = int(input(f"Enter number {i + 1}: "))
    num_list.append(num)

result = positiveNumbers(num_list)
print("Positive numbers:", result)