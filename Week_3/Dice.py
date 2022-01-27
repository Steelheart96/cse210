from distutils.command.clean import clean
from random import randint
from os import system
from time import sleep

def Clear(): system('cls')
def Wait(wait_time):  sleep(wait_time)

score = 0
roll_amount = 0
has_nums = True
YES_LIST = ['yes', 'ye', 'y']
NO_LIST = ['no','n']

while has_nums:
    die = []
    playing = ''
    while playing not in YES_LIST and playing not in NO_LIST:
        Clear()
        playing = input('Roll dice [y/n]? ').lower()

        if playing not in YES_LIST and playing not in NO_LIST:
            Clear()
            print(f'\'{playing}\' is not an accepted input, please try again.')
            Wait(3)
    
    if playing in NO_LIST: break

    for _ in range(5):
        die.append(randint(1,10))

    roll_amount += 1

    has_nums= False
    for dice in die:
        if dice == 1:
            has_nums = True
            score += 100
        elif dice == 5:
            has_nums = True
            score += 50
    
    print(f'You Rolled: ', end='')
    for i in range(0,5):
        print(die[i], end='')
        if i != 4: print(', ', end='')

    print(f'\nYour Rolls: {roll_amount}')
    print(f'Your score: {score}')
    

    if not has_nums:
        print('\nA five or a one is not amoung your die.')
        print('GAME OVER')

    Wait(3)

if playing in NO_LIST and roll_amount > 0:
    Clear()
    print(f'\nYour Rolls: {roll_amount}')
    print(f'Your score: {score}')
    print('GAME OVER')
    Wait(3)
elif playing in NO_LIST and roll_amount == 0:
    print('GAME OVER')
    Wait(3)