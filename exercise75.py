# Function that takes a string as an argument and returns the first and last characters as a tuple

def firstLastChar(string):
    if not string:
        return None
    
    firstChar = string[0]
    lastChar = string[-1]

    return(firstChar, lastChar)

