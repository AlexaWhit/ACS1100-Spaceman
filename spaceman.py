from mimetypes import guess_all_extensions
import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass



def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    print("------ WELCOME TO SPACEMAN!! ------\n *****Your secret word has been chosen*****\nPlease enter a letter you think si in the word: " )




# USER INPUT
def user_input(prompt):
    #input function will display message to user and wait for input
    user_input = input(prompt).lower() #allow for lower-case
    return user_input




    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

       
    #TODO: check if the game has been won or lost

#--------------------------VARIABLES-------------------------------#
incorrect_guesses = 7
guess = user_input("Please guess a letter to complete the Secret Word:  ")
letters_guessed = []
win = False



#-------------------------ACTUAL CODE HERE-------------------------#
# Welcome Message
print("----- Welcome to Spaceman -----")

# Need Instructions?
instructions = input("Do you need instructions? (Y/N/) > ")
if instructions.lower() == "y":
    print("Spaceman is a guessing game.\nThere is a mystery word which you will try to guess one letter at a time.\nA placeholder is initially shown, with the number of blanks corresponding to the number of letters in the word.\nIf the letter is in the mystery word, the position(s) of the letter(s) are revealed in the placeholders.\nGuess the word before you run out of guesses!\nYou will only be allowed 7 incorrect  guesses!\nGOOD LUCK!!")
else: 
    print("Good luck!")

#These function calls that will start the game



secret_word = load_word()
spaceman(secret_word)



#----- WHILE LOOP------#
#running: True
#while running:
#    guess = user_input("Please guess a letter to complete the Secret Word:  ")
    #running = select(guess)