# Program to remove duplicates from a list using a set

def remove_duplicate(input_list):
    unique_set = set(input_list)

    unique_list = list(unique_set)

    return unique_list

input_list = [10, 20, 30, 10, 40, 50, 20]

result = remove_duplicate(input_list)

print("Original list: ", input_list)
print("List without duplicates: ", result)