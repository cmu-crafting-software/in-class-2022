#Luis Viornery and Dan Connolly

import random

def compWord(guess,word):
    comp = ['x']*len(guess)
    for i in range(len(guess)):
        if guess[i] == word[i]:
            comp[i] = '!'
        elif guess[i] in word:
            comp[i] = 'o'
    return comp
    
def getWord(wordList):
    badGuess = True
    while(badGuess):
        guess = ''.join(filter(str.isalpha,input('Guess a five-letter word: '))).lower()
        if (len(guess) == 5 and ''.join(guess) in wordList):
            badGuess = False
        else:
            print('Bad input!')
    return guess

#initialize game state

f = open('sgb-words.txt')
flist = f.read().split('\n')
#select target word
word = random.choice(flist)
f.close()
maxTries = 6
win = False
for i in range(maxTries):
    #get user input
    guess = getWord(flist)

    #compare user input to target word
    comp = compWord(guess,word)

    #give user feedback
    print(guess)
    print(''.join(comp))
    if word == guess:
        win = True
        break
if win:
    #end game (win)
    print('your winner!')
else:
    #end game (lose)
    print('haha scrub')
