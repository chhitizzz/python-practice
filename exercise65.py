# Function that takes a list of numbers as an argument and returns the sum of all even numbers in the list

def even_numbers_sum (numbers):
    evenSum = 0

    for num in numbers:
        if num % 2 == 0:
            evenSum += num

    return evenSum

numCount = int(input("Enter the number of elements: "))
numList = []

for i in range(numCount):
    num = int(input(f"Enter number {i + 1}: "))
    numList.append(num)

print(f"The list is: {numList}")

result = even_numbers_sum(numList)
print(f"The sum of even numbers is {result}.")