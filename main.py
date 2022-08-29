from os import system, name

from src.game_cli import GameCli
from src.game import Game
from src.ship_placer import ShipPlacer


def get_user_inputs():
    while True:
        yield input('Your Move > ')

if __name__ == '__main__':
    config = {
        'columns': 10,
        'rows': 10,
        'ships': [
            {'name': 'B', 'length': 2},
            {'name': 'C', 'length': 3}
        ]
    }

    ship_placer = ShipPlacer(config)
    ship_coords = ship_placer.build_ship_coords()
    game = Game(ship_coords)

    cli = GameCli(get_user_inputs(), game)
    cli.run()

