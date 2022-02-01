#D'Nae Ferguson Lionel Sam

#Create a csv file of 5 letter words

# Randomly pick a word 
word = 'thorn'

#Some DS that holds a list of words 5 letters long

#Get user input 
guess = input("Guess a word, it must be 5 letters long: ")

    # bounded to only 5 letters
    # should be an actual word
    # break after 6 guesses

#Compare user input to stored word
def compareFirstPosition():
    if guess[0] == word[0]:
        print("*")
    elif (guess[0] == word[1]) | (guess[0] == word[2]) | (guess[0] == word[3]) | (guess[0] == word[4]):
        print("^")
    else: 
        print("_")

compareFirstPosition()

# Some type of graphic interface for user to see what's happening

# Provide feedback to user
    # if letter is in right spot = green
    # if letter is in wrong spot = yellow
    # if letter is not in word = gray
