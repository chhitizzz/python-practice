# Function that takes a string as an argument and returns a dictionary with the count of each character in the string

def count_characters(string):
    char_count = {}

    for char in string: 
        if char in char_count:
            char_count[char] += 1
        
        else: 
            char_count[char] = 1

    return char_count

input_string = input("Enter a string: ")

result = count_characters(input_string)
print("Character count: ", result)