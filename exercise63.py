# Function called `calculate_average` that takes a list of numbers as an argument and returns the average (mean) of the numbers

def calculate_average(numbers):
    if not numbers:
        return None
    
    total = sum(numbers)
    average = total / len(numbers)
    return average