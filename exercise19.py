# Program that generates a random number between 1 and 10 and asks the user to guess the number. The program should continue asking for guesses until the user guesses correctly.

import random

secret_number = random.randint(1, 10)

num = int(input("Guess a number between 1 to 10: "))

