# Function that takes a string as argument and prints its length

def stringLength(str):
    length_of_string = len(str) 
    return length_of_string

input_string = input("Enter a string: ")

result = stringLength(input_string)
print(f"The length of the string is {result}.")