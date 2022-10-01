from mimetypes import guess_all_extensions
import random

#--------------------------VARIABLES-------------------------------#
incorrect_guesses = 7
letters_guessed = []
win = False
guess = input("Incorrect guesses left: {incorrect_guesses}--> Please guess a letter:  ").upper()


#--------------------------FUNCTIONS-------------------------------#


def load_word():
#Reads text file of words and randomly selects one to use as the secret word
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word



def is_word_guessed(secret_word, letters_guessed):
#Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in range(len(letters_guessed)):
        if letters_guessed[letter] in secret_word:
            return True
        else:
            return False



def get_guessed_word(secret_word, letters_guessed):
#Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    correct_guess_string = ""
    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            correct_guess_string += secret_word[letter]
        else:
            correct_guess_string += "_"


 
def is_guess_in_word(guess, secret_word):
#check if the letter guess is in the secret word
    if guess in secret_word:
        print(f"Correct! {guess} appears in the word! ")
        return True
    else:
        print(f"Sorry! {guess} does not appear in the word.") 
        return False
    


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    print("------ WELCOME TO SPACEMAN!! ------\nYour secret word has been chosen at random and contains: {len(secret_word)} letters." )
    load_word()



def clearTerminal():
    print("\033[H\033[J")



def user_input(prompt):
    #input function will display message to user and wait for input
    user_input = input(prompt).upper() #allow for lower-case
    return user_input


  

#TODO: Ask the player to guess one letter per round and check that it is only one letter
player = False
while player == False:

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost 

    

    



#-------------------------ACTUAL CODE HERE-------------------------#
# Welcome Message
print("----- Welcome to Spaceman -----")

# Need Instructions?
instructions = input("Do you need instructions? (Y/N/) > ")
if instructions.lower() == "y":
    print(" \nSpaceman is a guessing game where you are only allowed 7 incorrect guesses.\nThere is a mystery word which you will try to guess one letter at a time.\nA placeholder is initially shown, with the number of blanks corresponding\nto the number of letters in the word. If the letter is in the mystery word,\nthe position(s) of the letter(s) are revealed in the placeholders.\n \nGuess the word before you run out of guesses!\nGOOD LUCK!!")
    clearTerminal()
else: 
    print("Good luck!")
    clearTerminal()

# Game Play
secret_word = load_word()
spaceman(secret_word)


# Ending
if win: 
    print(f"YOU WIN!! You guessed the Secret Word correctly!\nThe word was: {secret_word}.")
else: 
    print(f"***GAME OVER***\nThe word was: {secret_word}.")