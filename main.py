from os import system, name

from src.game_cli import GameCli

def get_user_inputs():
    while True:
        yield input('Your Move > ')

if __name__ == '__main__':
    cli = GameCli(get_user_inputs())
    cli.run()

