# Program to remove the vowels from a string

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for char in string:
    if char not in vowels: 
        result += char

print("String without vowels:", result)