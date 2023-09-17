# Program to remove duplicates from a list using a set

def remove_duplicate(input_list):
    unique_set = set(input_list)

    unique_list = list(unique_set)

    return unique_list