# Program to sort a dictionary by its keys

def sort_dict_by_keys(dictionary):
    sorted_dict = {k: dictionary[k] for k in sorted(dictionary.keys())}
    return sorted_dict

my_dict = {
    'b': 3,
    'a': 1,
    'c': 2
}