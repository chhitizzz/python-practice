# Program to find the key corresponding to the maximum value in a dictionary

def key_with_max_value(dictionary):
    if not dictionary:
        return None
    
    max_value = max(dictionary.values())
    for key, value in dictionary.items():
        if value == max_value:
            return key

my_dict = {'a': 10, 'b': 30, 'c': 20}

max_value_key = key_with_max_value(my_dict)

print("Key corresponding to maximum value:", max_value_key)