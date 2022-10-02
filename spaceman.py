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



def is_word_guessed(secret_word, correct_guesses):
#Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letters in range(len(secret_word)):
        if letters in correct_guesses:
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



def spaceman(secret_word):
    incorrect_guesses = 0
    correct_guesses = []
    letters_guessed = []
    game_running = True
    clearTerminal()
    #Show user information per project spec
    print(f"------ WELCOME TO SPACEMAN!! ------\nYour secret word has been chosen at random and contains: {len(secret_word)} letters.\nGuess one letter at a time, but if you have 7 incorrect guesses you will lose!.\n" )

    #Game Loops
    while game_running: 
        #Display num of incorrect guesses and letters guessed to the user
        print(f"Incorrect guesses: {incorrect_guesses} ")
        print(f"You have guessed the following letters: {letters_guessed}")
        #Display progress of the secret word to user
        print(get_guessed_word(secret_word, letters_guessed))
        #Request user to guess a new letter 
        guess = input("\nEnter a letter: ")

        #loop letter through secret word and display if it appears or not
        if is_guess_in_word(guess, secret_word) == True:
            print(f"Correct! {guess} appears in the word! ")
            #Add guessed letters to list
            correct_guesses.append(guess)
            letters_guessed.append(guess)
            #user wins if word is guessed       
            
        else:
            #Advise user if letter not in word and +1 to incorrect guesses
            print(f"Sorry! {guess} does not appear in the word.") 
            letters_guessed.append(guess)
            incorrect_guesses += 1

        #user wins if word is guessed    
        if is_word_guessed(secret_word, correct_guesses):
            print(f"\n***YOU WIN!!*** You guessed the Secret Word correctly!\nThe word was: {secret_word}\n") # Stretch Challenge: show the mystery word to the user at the en
            return
        #user loses if incorrect guesses = 7
        if incorrect_guesses >= 7:
            print(f"\n***GAME OVER***\nThe Secret Word was: {secret_word}\n")               
            return 

   

# Game Play
secret_word = load_word()
spaceman(secret_word)

 






    

    








