# Program to display powers of 2 using anonymous function 

nterms = int(input("Enter number of terms here: "))

result = list(map(lambda x : 2 ** x, range(nterms + 1)))

for i in range(nterms + 1):
    print(f"The value of 2 raised to the power {i} is {result[i]}")