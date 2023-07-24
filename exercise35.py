# Program to find the length of the longest word in a sentence

string = input("Enter a sentence: ")

words = string.split()

longest_word_length = 0

for word in words:
    word_length = len(word)
    if word_length > longest_word_length:
        longest_word_length = word_length

print(f"Length of the longest word is {longest_word_length}")