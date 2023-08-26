# Function that takes a list of numbers as an argument and returns a new list containing only the positive numbers

def positiveNumbers(numbers):
    positive_numbers = []

    for num in numbers: 
        if num > 0:
            positive_numbers.append(num)
        
    return positive_numbers