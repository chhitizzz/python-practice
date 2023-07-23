# Program to check if a given string is an anagram of another string

# Anagrams are formed by rearranging the letters of a word to create a new word, using all the original letters exactly once.

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

string1 = string1.replace(" ", " ").lower()
string2 = string2.replace(" ", " ").lower()

if len(string1) != len(string2):
    print("The strings are not anagram.")

else: 
    sorted_str1 = sorted(string1)
    sorted_str2 = sorted(string2)