# Program that generates a random number between 1 and 10 and asks the user to guess the number. The program should continue asking for guesses until the user guesses correctly.

import random

secret_number = random.randint(1, 10)

guess_number = 0

while guess_number != secret_number:
    guess_number = int(input("Guess the number (between 1 and 10): "))
