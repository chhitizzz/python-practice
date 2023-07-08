# Program that generates a random number between 1 and 20 and asks the user to guess the number. The program should continue asking for guesses until the user guesses correctly.

import random

secret_number = random.randint(1, 20)

guess_number = 0

while guess_number != secret_number:
    guess_number = int(input("Guess the number (between 1 and 20): "))

    if guess_number == secret_number:
        print("Congratulations! You have guessed the correct number.")

    else:
        print("Wrong guess. Try again.")


