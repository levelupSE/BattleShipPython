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


def get_ship_placement(ship_config, coord, direction):
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

    return potential_coords

def valid_coord(coord, rows, columns, ship_coords):
    row, col = coord
    return (
        row >= 0 and
        row <= rows - 1 and
        col >= 0 and
        col <= columns - 1 and
        coord not in ship_coords
    )

def get_valid_ship_placements(ship_coords, ship_config, rows, columns):
    available_coords = [
        coord
        for coord in get_coords(rows, columns)
        # exclude positions already placed
        if coord not in ship_coords
    ]

    random.shuffle(available_coords)

    for random_coord in available_coords:

        directions = [direction for direction in Direction]
        random.shuffle(directions)

        for random_direction in directions:
            potential_coords = get_ship_placement(ship_config, random_coord, random_direction)

            if all(valid_coord(coord, rows, columns, ship_coords) for coord in potential_coords):
                yield potential_coords

    return None



class ShipPlacer:

    def __init__(self, ship_configs, rows, columns, ship_coords, get_valid_ship_placements = get_valid_ship_placements):
        self.ship_configs = ship_configs
        self.rows = rows
        self.columns = columns
        self.ship_coords = ship_coords
        self._get_valid_ship_placements = get_valid_ship_placements

    def build_ship_coords(self):
        # create a copy of the list
        ships_to_place = self.ship_configs[:]

        for current_ship in ships_to_place:
            if not self._attempt_placement(self.ship_coords, current_ship):
                raise Exception('Could not place all ships on board')

        # transform to coords expected by game e.g. A1 -> A10
        return {
            (index_to_letter(row), str(col + 1)): ship_name
            for (row, col), ship_name in self.ship_coords.items()
        }

    def _attempt_placement(self, ship_coords, ship_config):
        for potential_placement in self._get_valid_ship_placements(ship_coords, ship_config, self.rows, self.columns):
            if potential_placement is not None:
                for coord in potential_placement:
                    ship_coords[coord] = ship_config['name']
                return True

        return False
