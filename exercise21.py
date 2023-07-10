# Program that asks the user to enter a string and uses a loop to count the number of vowels (a, e, i, o, u) in the string.

string = input("Enter a string: ")
no_of_vowels = 0

for char in string:
    if char.lower() in 'aeiou':
        no_of_vowels += 1

print(f"The number of vowels in {string} is {no_of_vowels}.")