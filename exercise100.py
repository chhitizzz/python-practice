# Program to check if a given value exists in a dictionary

def check_value_existence(dictionary, value):
    return value in dictionary.values()

myDict = {
    'name': 'Viper',
    'ultimate': "Viper's Pit",
    'role': 'Controller'
}

value_to_check = 'Viper'

if check_value_existence(myDict, value_to_check):
    print(f"The value '{value_to_check}' exists in the dictionary.")

else:
    print(f"The value '{value_to_check}' does not exist in the dictionary.")