# Function that takes a list of strings and a search string as arguments and returns a list of strings containing the search string

def find_string_with_substring(stringList, searchString):
    result_list = []

    for string in stringList:
        if searchString in string: 
            result_list.append(string)

    return result_list

string_count = int(input("Enter the number of strings: "))
string_list = []

for i in range(string_count):
    string = input(f"Enter string {i + 1}: ")
    string_list.append(string)

search_string = input("Enter the search string: ")

result = find_string_with_substring(string_list, search_string)
print("Strings containing the search string: ", result)