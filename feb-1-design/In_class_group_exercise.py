

from turtle import position


def guess_word_checker(guessWord,targetWord) :
    answer = ""
    if guessWord == targetWord:
        return "*****"
    for position in range(0,5,1):
        #print(position)
        if guessWord[position] == targetWord[position]:
            #print("before"+answer)
            #answer = answer.join("*")
            answer += "*"
            #print("after"+answer)
        elif guessWord[position] in targetWord:
             #print("Found in target word")
            answer += "!"
        else:
            answer += "_"
    return answer
#for loop to check each character

print(guess_word_checker("piano","pizza"))
#print(guess_word_checker("piano","piano"))