# Function that takes a list of strings and a search string as arguments and returns a list of strings containing the search string

def find_string_with_substring(stringList, searchString):
    result_list = []

    for string in stringList:
        if searchString in string: 
            result_list.append(string)

    return result_list