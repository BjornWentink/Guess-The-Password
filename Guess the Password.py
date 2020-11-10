# This program is a word guessing/puzzle game.
# The user must guess the keyword before a certain number of guesses.
#
# Import needed python libraries.
import random

# This function drives the entire program.
def Main():
    # Assign variables and lists.
    strikes = 8
    winCondition = False
    allGuesses = []
    #    
    # Get key word and hint.
    wordAndHint = ImportWord()
    keyWord = wordAndHint[0]
    hint = wordAndHint[1]
    #
    # Greet the user.
    GreetUser(hint)
    #
    # Run the game.
    while winCondition == False and strikes > 0:
        # Get user's guess.
        allGuesses += GetUserGuess(keyWord, allGuesses)
        #
        # Set strike value based on wrong guesses.
        strikes = SetStrikeValue(allGuesses)
        #
        # Check if player won.
        winCondition = CheckWinCondition(keyWord, allGuesses)

    if winCondition == True:
        DisplayWord(keyWord, allGuesses)
        input('\nYou won!')

    if strikes == 0:
        input('\nYou lost :(')
# End of Main().           
        
# This function returns a random word from the library. 
def ImportWord():
    #
    # Function setup.
    wordLibrary = open('Guess the Password Library.txt', 'r')
    wordList = []
    keyWord = wordLibrary.readline()
    #
    # Transpose file's content into list.
    while keyWord != '':
        subjHint = wordLibrary.readline()
        keyWord = keyWord.rstrip('\n')
        subjHint = subjHint.rstrip('\n')
        wordList += [[keyWord, subjHint]]
        keyWord = wordLibrary.readline()
    wordLibrary.close()
    #   
    # Get list size.
    listSize = 0
    for index in wordList:
        index = 1
        listSize +=  index
    #        
    # Randomly select a keyword and its hint from list.
    randomSelection = random.randint(0,(listSize - 1))            
    wordAndHint = wordList[randomSelection]
    return wordAndHint

# This functions greets the user.
def GreetUser(hint):
    print('Welcome to Guess the Password.\nTo win, guess the correct letters to',
          'complete the word.\nThe hint is:  ', hint)

# This function gets user's guess.
def GetUserGuess(keyWord, allGuesses):
    #
    # Displays word.
    DisplayWord(keyWord, allGuesses)
    #
    # Get user guess.
    userGuess = input('\n\nGuess a letter:  ')
    if userGuess.isalpha:
        userGuess = userGuess.lower()
    #
    # Condition if user's guess incorrect.
    if userGuess not in keyWord:
        return '!'
    #
    # Condition if guess was correct.
    else:
        return userGuess

# Displays word.
def DisplayWord(keyWord, allGuesses):
    # Seperate iteration.
    #
    print('_______________________________________\n')
    #
    # Display blank key word with filled in right answers to user.
    for letter in keyWord:
        if letter in allGuesses:
            print(letter, ' ', end='')
        else:
            if letter == ' ':
                print('  ', end='')
            else:
                print('_ ', end='')

# This function counts wrong answers and returns the strike value
def SetStrikeValue(allGuesses):
    strikes = 8
    #
    # Count incorrect answers
    for guess in allGuesses:
        if guess == '!':
            strikes -= 1
    #
    # Returns new value.
    print('\nStrikes left:  ', strikes)
    return strikes

# This function checks if player guessed the entire word.
def CheckWinCondition(keyWord, allGuesses):
    # Set up variables
    letterCount = 0
    correctCount = 0
    #
    # Counts letters in word and correct guesses
    for letter in keyWord:
        if letter != ' ':
            letterCount += 1
        if letter in allGuesses:
            correctCount += 1
    #
    # Compares number of correct guesses needed to win.
    if correctCount == letterCount:
        return True
    else:
        return False
            
# Call main.
Main()
