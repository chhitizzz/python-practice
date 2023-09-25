# Program to get a list of all keys in a dictionary

def get_all_keys(dictionary):
    return list(dictionary.keys())

myDict = {
    'name': 'Rodgers',
    'state': 'Wisconsin',
    'team': 'Packers'
}

keys_list = get_all_keys(myDict)

print("List of keys:", keys_list)