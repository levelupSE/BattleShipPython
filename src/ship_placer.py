import random
from enum import Enum

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

def index_to_letter(index):
    a_int = 97
    return chr(a_int + index)

def get_coords(rows, columns):
    return [
        (row_index, col_index)
        for col_index in range(columns)
        for row_index in range(rows)
    ]

class ShipPlacer:

    def __init__(self, config):
        self.ship_configs = config['ships']
        self.columns = config['columns']
        self.rows = config['rows']
        self.ship_coords = {}

    def build_ship_coords(self):
        # create a copy of the list
        ships_to_place = self.ship_configs[:]

        while ships_to_place:
            current_ship = ships_to_place.pop()
            placed = self._attempt_placement(current_ship)

            if not placed:
                raise Exception('Could not place all ships on board')

        # transform to coords expected by game e.g. A1 -> A10
        return {
            (index_to_letter(row), str(col + 1)): ship_name
            for (row, col), ship_name in self.ship_coords.items()
        }

    def _attempt_placement(self, ship_config):
        available_coords = [
            coord
            for coord in get_coords(self.rows, self.columns)
            # exclude positions already placed
            if coord not in self.ship_coords
        ]

        if not available_coords:
            return False

        while available_coords:
            random_coord = available_coords.pop(random.randrange(len(available_coords)))

            directions = [direction for direction in Direction]
            while directions:
                random_direction = directions.pop(random.randrange(len(directions)))
                placed = self._place_ship(ship_config, random_coord, random_direction)
                if placed:
                    return True

        return False

    def _place_ship(self, ship_config, coord, direction):
        '''Places ship on coordinate in specified direction if able to.'''

        ship_size = ship_config['length']

        # next_coord = lambda row, col, idx: None
        if direction == Direction.UP:
            next_coord = lambda row, col, idx: (row - idx, col)
        elif direction == Direction.DOWN:
            next_coord = lambda row, col, idx: (row + idx, col)
        elif direction == Direction.RIGHT:
            next_coord = lambda row, col, idx: (row, col + idx)
        elif direction == Direction.LEFT:
            next_coord = lambda row, col, idx: (row, col - idx)
        else:
            raise Exception('No valid direction provided')

        row, col = coord
        potential_coords = []
        for i in range(ship_size):
            potential_coords.append(next_coord(row, col, i))

        if all(self._valid_coord(coord) for coord in potential_coords):
            for coord in potential_coords:
                self.ship_coords[coord] = ship_config['name']
            return True

        return False


    def _valid_coord(self, coord):
        row, col = coord
        return (
            row >= 0 and
            row <= self.rows - 1 and
            col >= 0 and
            col <= self.columns - 1
        )
