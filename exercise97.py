# Program to check if a given key exists in a dictionary

def check_key_existence(dictionary, key):
    return key in dictionary    

myDict = {
    'firstName': 'Joe',
    'lastName': 'Mama',
    'age': 27
}

key_to_check = 'firstName'