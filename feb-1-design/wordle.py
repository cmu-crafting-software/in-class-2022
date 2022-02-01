# Yincheng and Shilin

# build a dictionary (5 letter words only)
# generate a random word from the dictionary
# get user input (limit to 5 letters each line)
from locale import THOUSEP


def getUserInput():
    guess = input('Enter your guess: ')
    return guess
    # prompt user to do another line for a total of 6 lines

# ? convert letters to numbers so that it's easier for comparison
# compare the input and the chosen word letter by letter and generate feedback
    # check if it's in dictionary
"""
inputs:   guess, the user's input, assume it's valid
          correct_word, the correct word
outputs:  a string of character of length 5
            _ represents the letter is not in the word
            * means the letter is in the correct word but not in the right position
            ^ means the letter is in the correct word and at the right position
"""          
def compareTwoWords(guess, correct_word):
    output = ""
    for i in range(len(guess)):
        # check which letters are used in the chosen word
        if correct_word.count(guess[i])==0:
            # the letter is not in the word
            output += "_"
         # check if the used letters are in the right position
        elif guess[i] == correct_word[i]:
            output += "^"
        else:
            output += "*"
    return output
   
# testing

guess = getUserInput()
print(compareTwoWords(guess,'aaaaa'))
print(compareTwoWords('aaple','aaaaa'))
print(compareTwoWords('apple','baaaa'))