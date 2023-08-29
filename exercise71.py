# Function that calculates the power of a number. It should have a default exponent of 2

def calculate_power(base, exponent=2):
    result = base ** exponent
    return result 

base_number = int(input("Enter the base number: "))
exponent_number = int(input("Enter the exponent number: "))

result = calculate_power(base_number, exponent_number)
print(f"{base_number} raised to the power of {exponent_number} is {result}")