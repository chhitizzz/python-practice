# Function that takes a list of numbers as an argument and returns the sum of all even numbers in the list

def even_numbers_sum (numbers):
    evenSum = 0

    for num in numbers:
        if num % 2 == 0:
            evenSum += num