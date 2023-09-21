# Program to access the value associated with a specific key in a dictionary

def accessDictionary(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    
    else:
        return None

myDict = {
    'name': 'Subhu',
    'age': 22,
    'country': 'Nepal'
}

