# Function that generates a random password of a given length. Allow the function to include letters, digits, and special characters

import random 
import string 

def generatePassword(length):
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    character = letters + digits + special_characters

    password = ''.join(random.choice(character) for _ in range(length))

    return password

password_length = int(input("Enter the desired password length: "))

password = generatePassword(password_length)
print(f"Your password is: ", password)