from os import system, name

from src.game_cli import GameCli
from src.game import Game

def get_user_inputs():
    while True:
        yield input('Your Move > ')

if __name__ == '__main__':

    game = Game({
        ('a', '1'): 'B',
        ('a', '2'): 'B',
        ('c', '3'): 'D',
        ('c', '4'): 'D',
        ('c', '5'): 'D',
    })

    cli = GameCli(get_user_inputs(), game)
    cli.run()

