# Program to check if a character is a vowel or consonant

character = input("Enter a character: ")

if character.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(f"{character} is a vowel")

else:
    print(f"{character} is a consonant")