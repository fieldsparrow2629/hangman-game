#hangman game
import random


word_bank = ['tree', 'alligator', 'aeroplane',]
word = random.choice(word_bank)

#a list of the correctly guessed letters
correct_letters = []

#shows the game is on
game = True

print("Hint: the word is " + str(len(word)) + " letters long")

tries = 10

def check_try(guess):
    
    #checks if guess is only one letter
    if len(guess) == 1:
        
        #check if letter is in the word
        if not guess in word:
            print("wrong")
                
        elif guess in correct_letters:
            print("you already guessed this")
            
        else:
            n = 0
            
            #loops through the word
            for a in word:

                #checks where the letters matches up
                if guess == a:
                    
                    #adds the guessed letter, and the index of the letter to the correct word list
                    correct_letters.insert(n,guess)
                    n += 1
                    
                else:
                    n += 1
            
    #if you guess the word correctly you win
    elif guess == word:
        print("You win!")
        
    else:
        print('only guess one letter at a time')


#while the game loop is running
while game == True:

    #asks for the guess lettter
    guess = raw_input("what is your guess?:" )
    check_try(guess)
    tries -= 1

    #if the guess is the correct word, game loop ends
    if guess == word:
        game = False
        break
    
    print("you have " + str(tries) + " tries left")
    print(correct_letters)

    #if you guess all the correct letter, you win, game loop ends
    if list(word) == correct_letters:
        print('you win')
        game = False

    #if you run out of tries, game loop ends
    if tries == 0:
        print('game over')
        game = False






