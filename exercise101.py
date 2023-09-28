# Program to iterate over the key-value pairs of a dictionary

def iterate_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

my_dict = {
    'name': 'Alice', 
    'age': 30, 
    'city': 'New York'
    }

iterate_dictionary(my_dict)