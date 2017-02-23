# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:12:42 2016

@author: manmeensaini
"""

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    numGuesses = 8
    lettersGuessed = []
    copySecretWord = []
        
    for char in secretWord:
        copySecretWord.append(char)
    
    while (numGuesses > 0):
        #get user's guess
                #check if word is guessed and break if true
        if (isWordGuessed(secretWord, lettersGuessed)):
            print("-------------")
            print("Congratulations, you won!")
            break
        print("-------------")
        print("You have " + str(numGuesses) + " left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        
        #check if user's letter was already guessed
        if guess not in lettersGuessed and guess: 
            lettersGuessed.append(guess.lower())
            #check user's guess is one of the letters in the word
            if guess in copySecretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))

            else: 
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                numGuesses -= 1   
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
    if numGuesses == 0: 
        print("-------------")
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".") 
        
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    copySecretWord = []
   
    for char in secretWord:
        copySecretWord.append(char)

    for char in secretWord:
        if char in lettersGuessed:
            copySecretWord.remove(char)
   
    return not copySecretWord 
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    copySecretWord = []
        
    for char in secretWord:
        copySecretWord.append(char)

    loopCount = 0
    for char in secretWord:
        if char not in lettersGuessed:
            copySecretWord[loopCount] = '_ '
        loopCount += 1
   
    return ''.join(copySecretWord)
    
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    copyAlpha = []    
    
    for char in string.ascii_lowercase:
        copyAlpha.append(char)
    
    for char in lettersGuessed:
        copyAlpha.remove(char)
        
    return ''.join(copyAlpha)

hangman("apple")
hangman("google")
hangman("abrakadabra")
