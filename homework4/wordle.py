import sys
from random import random
def word_generator(words):
    index = int(random() * len(words))
    secret_word = words[index]
    return secret_word
def guess_check(secret_word, guess):
    result=[]; i=0
    while i<word_lenghts:
        try:
            character = guess[i]
        except IndexError:
            print("Wrong length. Expected 5")
            sys.exit()
        if character==secret_word[i]:
            result.append('correct')
        elif character in secret_word:
            result.append('present')
        else:
            result.append('absent')
        i+=1
    return result   
def results(result, guess):
    display=[]
    j=0   
    while j<word_lenghts:
        try:
            symbol = guess[j]
        except IndexError:
            print("Wrong length. Expected 5")
            sys.exit()
        res = result[j]
        if res=='correct':
            display.append("["+symbol.upper()+"]")
        elif res=='present':
            display.append("("+symbol+")")
        else:
            display.append(" "+symbol+" ")
        j+=1
    return display

while True:
    words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
    secret_word=word_generator(words)
    tries=6
    word_lenghts = len(secret_word)
    print("Welcome to Wordle!")
    print("Guess the",word_lenghts,"-letter word. You have", tries, "tries.")
    while tries>0:
        guess = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower()
        if guess==secret_word:
            print("You win!!!")
            break
        result=guess_check(secret_word, guess)
        display = results(result, guess)
        print("Result:", ' '.join(display))
        tries -= 1
    else:
        print("You lose! The word was:", secret_word)
    next_game=int(input("Input 0 to exit and 1 to go next: "))
    if next_game ==0:
        break
    else:
        pass







