# Function that takes a list of numbers and a function as arguments and applies the function to each element of the list

def apply_function_to_list(numbers, custom_function):
    result = []
    for num in numbers:
        result.append(custom_function(num))
    return result

def square(x):
    return x * x

num_count = int(input("Enter the number of elements: "))
num_list = []

for i in range(num_count):
    num = float(input(f"Enter number {i + 1}: "))
    num_list.append(num)

result = apply_function_to_list(num_list, square)
print("Result after applying the function:", result)