# Program to replace all occurrences of a specific word in a string with another word

user_input = input("Enter a string: ")
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the replacement word: ")

words = user_input.split()

for i in range(len(words)):
    if words[i] == word_to_replace:
        words[i] = replacement_word

result = ' '.join(words)

print("Result:", result)