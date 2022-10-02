import random



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
    return correct_guess_string


 
def is_guess_in_word(guess, secret_word):
#check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False


def user_input(prompt):
    #input function will display message to user and wait for input
    user_input = input(prompt).upper() #allow for lower-case
    return user_input



def clearTerminal():
    print("\033[H\033[J")



def needInstructions():
    clearTerminal()
    print("----- Welcome to Spaceman -----")
    instructions = input("Do you need instructions? (Y/N): ").upper()
    if instructions == "Y":
        print(" \nSpaceman is a guessing game where you are only allowed 7 incorrect guesses.\nThere is a mystery word which you will try to guess one letter at a time.\nA placeholder is initially shown, with the number of blanks corresponding\nto the number of letters in the word. If the letter is in the mystery word,\nthe position(s) of the letter(s) are revealed in the placeholders.\n \nGuess the word before you run out of guesses!\nGOOD LUCK!!")
    else: 
        print("Good luck!")



def spaceman(secret_word):
    clearTerminal()
    needInstructions()
    clearTerminal()
    print(f"------ WELCOME TO SPACEMAN!! ------\nYour secret word has been chosen at random and contains: {len(secret_word)} letters.\nYou are allowed a maximum of 7 incorrect guesses.\n" )
    incorrect_guesses = 0
    correct_guesses = []
    letters_guessed = []
    while incorrect_guesses < 7:
        print(f"Incorrect guesses: {incorrect_guesses} ")
        print(f"You have guessed the following letters: {letters_guessed}")
        print(get_guessed_word(secret_word, letters_guessed))
        guess = input("\nEnter a letter: ")
        is_guess_in_word(guess, secret_word)
        if is_guess_in_word == True:
            print(f"Correct! {guess} appears in the word! ")
            correct_guesses.append(guess)
            letters_guessed.append(guess)
        else:
            print(f"Sorry! {guess} does not appear in the word.") 
            letters_guessed.append(guess)
            incorrect_guesses += 1
    if is_word_guessed == True:
        print(f"***YOU WIN!!*** You guessed the Secret Word correctly!\nThe word was: {secret_word}.") # Stretch Challenge: show the mystery word to the user at the end
    else: 
        print(f"***GAME OVER***\nThe Secret Word was: {secret_word}.") # Stretch Challenge: show the mystery word to the user at the end
    


# Game Play
secret_word = load_word()
spaceman(secret_word)

 
  





    

    








