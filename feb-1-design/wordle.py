# in class 2-1-22 Taryn and Dominic 


#Get a dictionary of words
#Pick a word (random)
#Query the user for the quess
#Counter for user guesses

secret = "beach"
guess = "check"



#Check if user guess is a word
    #If not, notify user

#Comparator
    
    #Check if letter is right and in the right position
    #Check if the user guessed letter are present at all
    #Check if user guessed letter is present but in the wrong spot
def compare(sword, gword):
    sword = sword.lower()
    gword = gword.lower()
    result = []

    if sword == gword: print("Congrats! You won Wordle!")

    for i in range(0,4,1):
        for j in range(0,4,1):
            if gword[i] == secret[j] and i == j: result.append("*")


    
    
    print("_ = totally incorrect, * = right letter in right place; ^ right letter, wrong position")
    return 

#Notify user of outcome and provide feedback
#Loop from comparator until user either guesses word or runs out of guesses




