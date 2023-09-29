# Program to merge two dictionaries into a new dictionary

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2) 
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = merge_dicts(dict1, dict2)

print("Merged dictionary:", merged_dict)