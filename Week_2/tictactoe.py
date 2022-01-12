'''
Assignment: W02 Prove: Developer - Solo Code Submission (Tic Tac Toe)
Author: Eric Woll
'''

import os

def make_board():
    spaces = {}
    for i in range(9):
        spaces[str(i+1)] = ' '
    return spaces
        
def render_board(spaces:dict):
    space = 1
    for i in range(0,3):
        print(f'{spaces[str(space)]}|{spaces[str(space+1)]}|{spaces[str(space+2)]}')
        if i < 2:
            print('-+-+-')
        space += 3

def choose_space(board, user):
    square_check = False
    while not square_check:
        render_board(board)
        square = input(f'{user}\'s turn to choose a square (1-9): ')
        square_check = check_board_space(board, square)
        Clear()
    return square

def set_space(board, square, user):
    board[square] = user

def check_board_space(board, square):
    if board[square] == ' ' and (board[square] != 'X' or board[square] != 'O'):
        return True
    return False

def tie_check(board):
    for square in range(1, 9):
        if board[str(square)] != 'X' and board[str(square)] != 'O':
            return False
    return True

def win_check(board:dict):
     return (board['7'] == board['8'] == board['9'] != ' ' or
        board['4'] == board['5'] == board['6'] != ' ' or
        board['1'] == board['2'] == board['3'] != ' ' or
        board['1'] == board['4'] == board['7'] != ' ' or 
        board['2'] == board['5'] == board['8'] != ' ' or
        board['3'] == board['6'] == board['9'] != ' ' or
        board['7'] == board['5'] == board['3'] != ' ' or
        board['1'] == board['5'] == board['9'] != ' ')

def switch_turn(current):
    if current == ' ' or current == 'X':
        return 'O'
    if current == 'O':
        return 'X'

def Clear(): os.system('cls')

def main():
    current_turn = switch_turn(' ')
    game_board = make_board()
    
    while not tie_check(game_board) and not win_check(game_board):
        square = choose_space(game_board, current_turn)
        set_space(game_board, square, current_turn)
        current_turn = switch_turn(current_turn)
    
    render_board(game_board)
    current_turn = switch_turn(current_turn)
    print(f'{current_turn} Won! Thanks for playing!')


if __name__ == '__main__':
    main()