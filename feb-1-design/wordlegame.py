#D'Nae Ferguson in class

#Compare user input to stored word
def guess_word_checker(guessWord, targetWord):
    #create empty answer variable 
    answer = ""
    #Check if guess is target word and return all stats
    if guessWord == targetWord:
        return "*****"
    for position in range(0,5,1):
        if guessWord[position] == targetWord[position]:
            answer += "*"
        elif guessWord[position] in targetWord:
            answer += "^"
        else:
            answer += "_"
    return answer

guess_word_checker("pizza", "piano")
