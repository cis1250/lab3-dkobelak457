#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# validation loop
user_sentence = input("Enter a sentence: ")
while is_sentence(user_sentence) == False:
    print("This does not meet the criteria for a sentence (Must start with a capital letter and end with .!?).")
    user_sentence = input("Enter a valid sentence: ")

#converts all the words to lowercase
lower_sentence = user_sentence.lower()
#re.sub is used to clean the sentences, ex replace capitals ect
cleaned_sentence = re.sub(r'[^\w\s]', ' ', lower_sentence)
#split is used to split the sentences up into indivudual strings
all_words = cleaned_sentence.split()

#Empty strings for words and frequency 
unique_words = []
frequencies = []

#for loop to get words and add them to a list 
# word is temporary, used to see if words are inside of the list
for word in all_words:
    if word: # Ensures only process non empty strings
        if word in unique_words:
            # If the word is already in the unique list, increment its count 
            index = unique_words.index(word)
            frequencies[index] += 1
        else:
            # If it's a new word, add it to the unique list and set its initial frequency to 1
            unique_words.append(word)
            frequencies.append(1)


print("\n Word Frequency Results ")
# Only print results if words were actually found
if unique_words:
# zip both unique words and frequencies for easy clean access 
    
    for word, count in unique_words, frequencies:
        print(f"'{word}': {count}")
else:
    print("No words found ") 
