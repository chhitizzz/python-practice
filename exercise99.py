# Program to get a list of all values in a dictionary

def get_all_values(dictionary):
    return list(dictionary.value())

myDict = {
    'name': 'Kobe',
    'team': 'LA Lakers',
    'position': 'Shooting Guard'
}