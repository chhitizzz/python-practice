# Function that takes a string as an argument and returns the first and last characters as a tuple

def firstLastChar(string):
    if not string:
        return None
    
    firstChar = string[0]
    lastChar = string[-1]

    return(firstChar, lastChar)

user_input = input("Enter a string: ")

print(f"The word is {user_input}.")

result = firstLastChar(user_input)

if result is not None:
    firstChar, lastChar = result
    print(f"The first character is '{firstChar}' and the last character is '{lastChar}'.")

else:
    print("The string is empty.")