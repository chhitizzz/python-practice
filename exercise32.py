# Program to remove the vowels from a string

string = input("Enter a string: ")

replacements = [('a', ""), ("e", ""), ("i", ""), ("o", ""), ("u", "")]

for char, replacement in replacements:
    if char in string: 
        string = string.lower().replace(char, replacement)

print(string)