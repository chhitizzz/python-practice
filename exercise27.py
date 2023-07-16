# Program to display powers of 2 using anonymous function 

nterms = int(input("Enter number of terms here: "))

result = map(lambda x : 2 ** x, range(nterms + 1))