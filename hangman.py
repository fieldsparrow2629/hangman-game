#hangman game
import random

word_bank = ['tree', 'alligator', 'aeroplane',]
word = random.choice(word_bank)
correct_letters = []
game = True
print("Hint: the word is " + str(len(word)) + " letters long")
tries = 10

def check_try(c):
    
    #checks if guess is only one letter
    if len(c) == 1:
        #check if letter is in the word
        if not c in word:
            print("wrong")
                
        #loops through the word
        elif c in correct_letters:
            print("you already guessed this")
        else:
            n = 0
            for a in word:
                if c == a:
                    correct_letters.insert(n,c)
                    n += 1
                else:
                    n += 1
            

    elif c == word:
        print("You win!")
        
    else:
        print('only guess one letter at a time')



while game == True:
    
    c = raw_input("what is your guess?:" )
    check_try(c)
    tries -= 1
    
    if c == word:
        game = False
        break
    
    print("you have " + str(tries) + " tries left")
    print(correct_letters)

    
    if list(word) == correct_letters:
        print('you win')
        game = False
    
    if tries == 0:
        print('game over')
        game = False






