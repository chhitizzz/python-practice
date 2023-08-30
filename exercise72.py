# Function that takes a sentence as an argument and returns a list of unique words. Allow the function to ignore case

def uniqueWords(sentence):
    words = sentence.lower().split()
    unique_words = set(words)
    return list(unique_words)