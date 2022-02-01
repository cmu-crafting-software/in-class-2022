#Darren and Jack Wordle Code


#Build Dictionary

#Build GUI

#Generate Random Word

#Get User Input

#Check User Input against randomly generated word
def comparison(user_guess,true_word) :
    for letter in user_guess:
        if user_guess[letter] == true_word[letter]:
            print('_')
        elif user_guess[letter] in true_word:
            print('*')
        else:
            print('^')

comparison('ideal','diner')
#Check word against dictionary

#Provide feedback to User 

#loop for 6 tries or until successful guess