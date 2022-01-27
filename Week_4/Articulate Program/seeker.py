from random import randint

def main():
    game = Director.initialize_game()
    run = True
    while run:
        isFound = Director.play(game)
        Response.give_response(isFound)
        if isFound == 'guessed': run =  False

class Director:

    def initialize_game() -> None:
        return Hider()

    def play(game):
        guess = Player.get_guess()
        return game.check_position(guess)
        

class Player:

    def get_guess():
        run = True
        while run:
            guess = Player.get_input()
            run = Player.isIncorrectInput(guess)
        return int(guess)

    def get_input():
        return input('Enter a Location [1-1000]: ')
    
    def isIncorrectInput(guess):
        try:
            guess = int(guess)
            if guess < 1 or guess > 1000:
                return True

            elif 0 < guess < 1001:
                return False
        except:
            return True


class Hider:

    def __init__(self) -> None:
        self._position = randint(1,1000)
    
    def check_position(self, guess):
        if self._position == guess: return 'guessed'
        
        elif abs(self._position - guess) <= 100: return 'warmer'

        else: return 'colder'


class Response:

    def give_response(position: str) -> None:
        if position == 'guessed':
            Response.found()
        elif position == 'colder':
            Response.cold()
        elif position == 'warmer':
            Response.warm()
    
    def warm():
        print('(>.<) Getting Warmer!')
    
    def cold():
        print('(^.^) Getting Colder!')
    
    def found():
        print('(;.;) You found me!')

if __name__ == '__main__':
    main()