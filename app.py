#Import random for word selection
import random

#Function that greets user, takes name and starts the game.
def welcome():
    name= input("Enter your name: ")
    print("Welcome", name, "to a game of hangman")
    print("#####################################")
    print("You have 10 tries to guess the word")
    hangman()

def hangman():
    #Array of words to be pulled from
    word = random.choice(['discount','reflect','photography','philosophy','empire','extend','slime'])
    #all letters available to use
    validLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Number of tries left
    tries = 10
    #Last letter guessed
    guessed=""

    while len(word) > 0:
        msg=""
        
        for letter in word:
            if letter in guessed:
                msg = msg + letter
            else:
                msg = msg + "_" + " "
                
        
        if msg == word:
            print(msg)
            print("You win, the word was", word, "!")
            break
        
        print("Guess the word:", msg)

        guess= input()

        if guess in validLetters:
            guessed = guessed + guess
        else:
            print("Enter a valid letter")

            guess = input()

        if guess not in word:
            tries = tries -1
            if tries == 9:
                print("Tries left:", tries)
            if tries == 8:
                print("Tries left:", tries)
            if tries == 7:
                print("Tries left:", tries)
            if tries == 6:
                print("Tries left:", tries)
            if tries == 5:
                print("Tries left:", tries)
            if tries == 4:
                print("Tries left:", tries)
            if tries == 3:
                print("Tries left:", tries)
            if tries == 2:
                print("Tries left:", tries)
            if tries == 1:
                print("Tries left:", tries)
            if tries == 0:
                print("You lose, the word was:", word)
                break



welcome()
            
        
