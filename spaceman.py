#pylint: disable=missing-module-docstring
#pylint: disable=redefined-outer-name
#pylint: disable=trailing-whitespace
#pylint: disable=line-too-long
import random

def load_word():
    '''
    A function that reads the text file of words and randomly selects one 
    from the list to use as the secret word.

    Returns:
    string: the secret word to be used in the spaceman game

    '''

    file = open('words.txt', 'r') #pylint: disable=unspecified-encoding 
    words_list = file.readlines()
    file.close()
    words_list = words_list[0].split(' ') 
    secret_word = random.choice(words_list)
    return secret_word



def is_word_guessed(secret_word, correct_guesses):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Parameters:
    secret_word (string): the random word the user is trying to guess.
    correct_guesses (list of strings): list of letters that have been guessed and are also in the secret word.

    Returns:
    bool: True only if all the letters of the secret_word are in correct_guesses, False otherwise.

    '''
    guess_is_correct = ""
    for letter in range(len(secret_word)):
        if secret_word[letter] in correct_guesses:
            guess_is_correct += secret_word[letter]
            if guess_is_correct == secret_word:
                return True
    return False
       


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters 
    guessed so far in the secret word and underscores 
    for letters that have not been guessed yet.

    Parameters:
    secret_word (string): the random word the user is trying to guess.
    letters_guessed (list of strings): list of letters that have been guessed by the user

    Returns:
    string: letters and underscores. For letters in the word that the user had guessed 
    correctly, the string should contain the letter at the correct position. For letters 
    in the word that the user has not yet guessed, shown an _ (underscore) instead.

    '''
    #Loop through the letters in secret word and build a string that shows the letters that 
    #have been guessed correctly so far that are saved in letters_guessed and underscores for 
    #the letters that have not been guessed yet
    correct_guess_string = ""
    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            correct_guess_string += secret_word[letter]
        else:
            correct_guess_string += "_"
    return correct_guess_string


 
def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Parameters:
    guess (string): The letter the player guessed this round
    secret_word (string): The secret word

    Returns:
    bool: True if the guess is in the secret_word, False otherwise
    '''
    #check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    return False



def clear_terminal():
    '''
    A function to clear the terminal for better readability

    Returns:
    a clear terminal
    '''
    print("\033[H\033[J")



def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Parameters:
    secret_word (string): the secret word to guess.

    '''
    incorrect_guesses = 0
    correct_guesses = []
    letters_guessed = []
    game_running = True
    clear_terminal()
    #Show user information per project spec
    print(f"------ WELCOME TO SPACEMAN!! ------\nYour secret word has been chosen at random and contains: {len(secret_word)} letters.\nGuess one letter at a time, but if you have 7 incorrect guesses you will lose!.\n" ) #pylit: disable=line-too-long

    #Game Loop:
    while game_running: 
        #Display num of incorrect guesses and letters guessed to the user
        print(f"Incorrect guesses: {incorrect_guesses} ")
        #Display list of the letters the user has already guessed
        print(f"You have guessed the following letters: {letters_guessed}")
        #Display progress of the secret word to user
        print(get_guessed_word(secret_word, letters_guessed))
        #Request user to guess a new letter 
        guess = input("\nEnter a letter: ")

        #loop letter through secret word and display if it appears or not
        if is_guess_in_word(guess, secret_word) is True:
            print(f"Correct! {guess} appears in the word! ")
            #Add guessed letters to list
            correct_guesses.append(guess)
            letters_guessed.append(guess)
        else:
            #Advise user if letter not in word, add quess to letters_guessed, and +1 to incorrect guesses
            print(f"Sorry! {guess} does not appear in the word.") 
            letters_guessed.append(guess)
            incorrect_guesses += 1

        #user wins if word is guessed    
        if is_word_guessed(secret_word, correct_guesses):
            # Stretch Challenge: show the mystery word to the user at the end
            print(f"\n*****YOU WIN!!****\n\nYou guessed the Secret Word correctly!\nThe word was: {secret_word}\n")
            return
        #user loses if incorrect guesses = 7
        if incorrect_guesses >= 7:
            # Stretch Challenge: show the mystery word to the user at the end
            print(f"\n***GAME OVER***\n\nSorry, you ran out of guesses!\nThe Secret Word was: {secret_word}\n")               
            return 

   
# Game Play
secret_word = load_word()
spaceman(secret_word)
