# Function that takes a list of strings and a function as arguments and returns a new list containing strings that satisfy the given function

def filter_strings(strings, custom_function):
    result = []
    for string in strings:
        if custom_function(string):
            result.append(string)
    return result

def contains_letter_a(text):
    return 'a' in text

string_count = int(input("Enter the number of strings: "))
string_list = []

for i in range(string_count):
    text = input(f"Enter string {i + 1}: ")
    string_list.append(text)

filtered_result = filter_strings(string_list, contains_letter_a)
print("Strings containing 'a':", filtered_result)