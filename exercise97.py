# Program to check if a given key exists in a dictionary

def check_key_existence(dictionary, key):
    return key in dictionary    

myDict = {
    'firstName': 'Joe',
    'lastName': 'Mama',
    'age': 27
}

key_to_check = 'name'

if check_key_existence(myDict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")

else: 
    print(f"The key '{key_to_check}' doesn't exist in the dictionary.")