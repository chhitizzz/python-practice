# Program to get a list of all values in a dictionary

def get_all_values(dictionary):
    return list(dictionary.values())

myDict = {
    'name': 'Kobe',
    'team': 'LA Lakers',
    'position': 'Shooting Guard'
}

values_list = get_all_values(myDict)

print("List of values: ", values_list)