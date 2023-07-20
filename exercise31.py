# Program to reverse a string

def reverse_string(input_string):
    return input_string[::-1]

string = input("Enter a string: ")
reverse_string = reverse_string(string)

print(f"Reversed string: {reverse_string}")