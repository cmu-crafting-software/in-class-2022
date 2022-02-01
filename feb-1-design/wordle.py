# Nikole and Katie 

# Import dictionary with english words
from english_words import english_words_set as words
# a = 'ghost' in words
# print(a)


# Get subset of dict with 5 letter words 
# Generate a five letter word 

# Loop 6 times: 
# Get keyboard input from user 
# Confirm input is 5 letters
# Convert input to lowercase/upper case (dependent on dict?)
# Check if input is a word 
# Compare user input string to generated string by index 
true_word = 'ghost'
guess_word = 'toast'
def compare_words(guess_word, true_word):
    solution = []
    found = []
    for guess, true in zip(guess_word, true_word):
        for guess, true in 
        if guess == true:
            solution.append(guess.upper())
            found.append(guess)
        elif guess in true_word: 
            solution.append(guess.lower())
        else:
            solution.append('_')
    print(solution)
        
compare_words(guess_word, true_word)

# Generate if statement that tells the user inputed entry matches generated word
# Break if all correct 

