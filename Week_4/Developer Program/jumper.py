'''
Assignment: Week 04: Jumper
Author: Eric Woll
'''

from random import choice
from os import system
from time import sleep

def main():
    word = WordList.find_one('words.txt')
    characters = WordGuess.break_word(word)
    characters = WordGuess.fill(characters)

    lives = 4

    run = True
    while run:

        no_input = True
        while no_input:

            Helper.clear()
            Helper.display(characters)

            user_guess = UserInput.retrieve('Guess a letter [a-z]: ')
            no_input = UserInput.isBadInput(user_guess)
            if no_input:
                print('That input is not accepted.')
                Helper.wait()

        if GuessCheck.check_spot(user_guess, characters):

            if GuessCheck.isCorrect(characters, user_guess):
                characters = WordGuess.update(user_guess, characters)
            else:
                Parachute.remove_line()
                lives -= 1

        else:
            print(f'You already Guessed "{user_guess.lower()}".')
            Helper.wait()
            Parachute.remove_line()
            lives -= 1
            
        run = WordGuess.isIncomplete(characters)

        if lives == 0:
            run = False
    
    Helper.clear()
    Helper.display(characters)

    if lives == 0:
        print('Your person fell!')
        WordGuess.show_word(characters)
    else:
        print('Your person has made it safely to the ground!')


class Helper:
    '''General Helper functions'''

    def clear(): system('cls')

    def wait(): sleep(3)

    def display(characters):
        WordGuess.display(characters)
        print()
        Parachute.display()


class WordList:
    '''Reads a text file and returns it as a list'''
    
    def read_file(text_file) -> list:
        with open(text_file) as file:
            words = file.readlines()
        return words 
        
    def strip_list(list: list) -> list:
        return [item.strip() for item in list]

    def find_one(text_file:str) -> str:
        words = WordList.read_file(text_file)
        words = WordList.strip_list(words)
        return choice(words)


class WordGuess:
    '''Displays and manages the word to guess'''

    def break_word(word:str) -> list:
        '''Breaks word into a list of characters'''
        return [char for char in word]
        
    def fill(characters:list) -> list:
        '''Fills guessed character list with '_' '''
        word = []
        for letter in characters:
            word.append([letter, '_'])
        return word

    def display(characters: list) -> None:
        '''Displays guessed character list'''
        for letter in range(len(characters)):
            print(characters[letter][1], end=' ')

    def update(user_guess: str, word: list) -> list:
        '''Updates guessed character list'''
        for letter in word:
            if letter[0] == user_guess.lower():
                letter[1] = letter[0]
        return word
    
    def isIncomplete(word: str) -> bool:
        '''Checks for '_' in guesse list'''
        check = []
        for letter in word:
            if letter[1] == '_': check.append('False')
        else: check.append('True')

        if 'False' in check: return True
        else: return False

    def show_word(characters:list) -> None:
        '''Shows the word player had to guess for current round'''
        new_list = [char[0] for char in characters]
        print('Your word was: ', end='')
        for item in new_list:
            print(item, end='')
        print()


class Parachute:
    '''Displays and manages the parachute character'''

    image = [   '  ___',
                ' /___\\',
                ' \\   /',
                '  \\ /',
                '   o',
                '  /|\\',
                '  / \\',
                '',
                '^^^^^^^'  ]
    
    list_num = 0

    def display() -> None:
        '''Displays parachute'''
        for i in range(Parachute.list_num, len(Parachute.image)):
            print(Parachute.image[i])
    
    def remove_line() -> None:
        'stops line(s) from displaying on Parachute'
        Parachute.list_num += 1


class UserInput:
    '''Retrieves user input and returns a single character'''

    def retrieve(display_message:str) -> str:
        '''Retrieves user input'''
        return input(display_message)
    
    def isBadInput(user_input:str) -> bool:
        '''Checks for incorrect user input'''
        if len(user_input) > 1 or len(user_input) == 0:
            return True
        else:
            if user_input.isnumeric(): return True
            else: return False


class GuessCheck:
    '''Checks user's guess against the word'''

    def isCorrect(characters:list, user_guess:str) -> bool:
        '''Check to see if user guess is correct'''
        new_list = [char[0] for char in characters]

        if user_guess.lower() in new_list: return True
        else: return False
    
    def check_spot(user_guess, word):
        for letter in word:
            if letter[0] == user_guess.lower():
                if letter[1] != '_':
                    return False
        return True


if __name__ == '__main__':
    main()