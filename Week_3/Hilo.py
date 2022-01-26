'''
Author: Eric Woll
Assignment: Week 3 Hilo
'''

from random import randint
from operator import gt, lt
from os import system

POINT_GAIN = 100
POINT_LOSS = 75

# gt -> Greator Than | lt - > Less Than
OPERATORS = {'higher': gt, 'lower': lt}

YES_LIST = ['yes', 'ye', 'y']
NO_LIST = ['no', 'n']


def main():
    Clear()
    STARTING_SCORE = 300

    player_score = Score(STARTING_SCORE, POINT_GAIN, POINT_LOSS)
    game_cards = Card()

    run = True
    while run:

        user_guess = ''
        while user_guess == '':
            display_info(is_guess_stage=True, current_card=game_cards.current_card, score=player_score.score)
            user_guess = process_guess('Higher or Lower? ')
            Clear()

        is_correct_guess = game_cards.card_guess_check(user_guess)

        if is_correct_guess:
            player_score.add_points()
        else:
            player_score.remove_points()
    
        again = ''
        while again == '':

            if is_correct_guess:
                print('Correct, you now have 100 more points!\n')
            else:
                print('Incorrect, you have lost 75 points.\n')

            display_info(is_guess_stage=False, current_card=game_cards.current_card, new_card=game_cards.new_card,
            user_guess=user_guess, score=player_score.score)
            print()
            
            again = input('Would you like to continue? ').lower()

            if again in NO_LIST:
                break
            elif again not in YES_LIST:
                again = ''

        Clear()
        game_cards.roll_new_card()


def Clear():
    '''Clears the Terminal.'''
    system('cls')

def display_info(is_guess_stage:bool, current_card:int, new_card:int=None, user_guess:str=None, score:int=None):
    '''
    Displays the current game information.
    '''
    if is_guess_stage:
        print(f'Current Card: {current_card}')
        print(f'Your Score: {score}')
    else:
        print(f'Current Card: {current_card}')
        print(f'Your Guess: {user_guess}')
        print(f'Next Card Was: {new_card}')
        print(f'Your Score: {score}')

def process_guess(display_msg:str) -> str:
    '''
    Takes in and checks player input for incorrect input.\n
    Returns player input.
    '''
    user_input = ''
    try:
        user_input = input(f'{display_msg}').lower()
        
        if user_input == 'h':
            user_input = 'higher'
        elif user_input == 'l':
            user_input = 'lower'
        else:
            user_input = ''
            raise ValueError

    except (ValueError, KeyError):
        print('You did not enter an accepted input, please try again.')
        
    return user_input


class Score:
    '''
    Holds and manages the players score.
    '''

    def __init__(self, starting_score:int, point_gain:int, point_loss:int):
        self.score = starting_score
        self.p_gain = point_gain
        self.p_loss = point_loss
    
    def remove_points(self):
        '''Removes a set amount of points from the player score.'''
        self.score -= self.p_loss
    
    def add_points(self):
        '''Adds a set amount of points to the player score.'''
        self.score += self.p_gain
    
    def is_zero(self) -> bool:
        '''Checks if the player score is Zero.'''
        if self.score <= 0: return True
        else: return False


class Card:
    '''
    Holds and manages the current_card, new_card, and user_guess.
    '''

    def __init__(self):
        '''current_card and new_card are automatically assigned a value on the creation of an instance.'''
        self.current_card = randint(1,13)
        self.new_card = randint(1,13)
        self.roll_check()

    def roll_new_card(self):
        '''Assigns new_card a new value.'''
        self.current_card = self.new_card
        self.new_card = randint(1,13)
        self.roll_check()
    
    def roll_check(self):
        '''Checks if new_card is equall to current_card. If it is, a new value is assigned to new_card.'''
        same_num = True
        while same_num:
            if self.current_card == self.new_card:
                self.new_card = randint(1,13)
            else:
                same_num = False
    
    def card_guess_check(self, user_guess:str) -> bool:
        '''Checks to see if user_guess is correct.'''
        if OPERATORS[user_guess](self.new_card, self.current_card):
            return True
        else:
            return False

    
if __name__ == '__main__':
    main()