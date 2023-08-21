# Function called `calculate_average` that takes a list of numbers as an argument and returns the average (mean) of the numbers

def calculate_average(numbers):
    if not numbers:
        return None
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

num_count = int(input("Enter the number of elements: "))
num_list = []

for i in range(num_count):
    num = float(input(f"Enter number {i + 1}: "))
    num_list.append(num)

average_result = calculate_average(num_list)

if average_result is not None: 
    print(f"The average of the numbers is {average_result:.2f}")

else:
    print("The list is empty.")