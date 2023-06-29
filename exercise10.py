# Program to check if a character is a vowel or consonant

character = input("Enter a letter: ")

vowel = ['a', 'e', 'i', 'o', 'u']

if character == vowel:
    print(f"{character} is a vowel")

else:
    print(f"{character} is a consonant")