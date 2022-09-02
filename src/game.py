from enum import Enum
from dataclasses import dataclass

class CoordStatus(Enum):
    '''Status of a board coordinate'''
    SHIP_HIT = 1
    SHIP_MISSED = 2
    EMPTY = 3

    def __repr__(self):
        return self.name

class AttackResult(Enum):
    SUCCESS = 1
    MISSED = 2
    INVALID = 3

@dataclass
class CoordInfo:
    status: CoordStatus
    ship_name: str

    def __repr__(self):
        if self.status == CoordStatus.SHIP_HIT:
            return self.ship_name
        if self.status == CoordStatus.SHIP_MISSED:
            return 'x'
        if self.status == CoordStatus.EMPTY:
            return ' '
        return 'n/a'

def letter_to_index(letter):
    letter_int = ord(letter)
    return letter_int - 97

def to_coordinates(row, col):
    '''Translates user provided input to zero index based matrix coordates: e.g. A1 -> (0, 0).'''
    row_index = letter_to_index(row)
    col_index = int(col) - 1
    return (row_index, col_index)


class Game:
    def __init__(self, ship_coords, col_length = 10, row_length = 10):
        self.attacked_coords = set()
        self.ship_coords = ship_coords
        self.row_length = row_length
        self.col_length = col_length

    def attack(self, row, col):
        coord = to_coordinates(row, col)

        if not self._on_board(coord):
            return AttackResult.INVALID

        # already attacked that position
        if coord in self.attacked_coords:
            return AttackResult.MISSED

        self.attacked_coords.add(coord)
        if coord in self.ship_coords:
            return AttackResult.SUCCESS

        return AttackResult.MISSED


    def game_over(self):
        attacked_ship_coords = self.attacked_coords.intersection(set(self.ship_coords.keys()))
        return len(attacked_ship_coords) == len(self.ship_coords)

    def get_board_layout(self):
        return [
            [self._get_coord_status(row_index, col_index) for col_index in range(self.col_length) ]
            for row_index in range(self.row_length)
        ]

    def _get_coord_status(self, row, col):
        coord = (row, col)

        if coord in self.attacked_coords and coord in self.ship_coords:
            return CoordInfo(CoordStatus.SHIP_HIT, self.ship_coords[coord])

        if coord in self.attacked_coords:
            return CoordInfo(CoordStatus.SHIP_MISSED, None)

        return CoordInfo(CoordStatus.EMPTY, None)

    def _on_board(self, coord):
        (row_index, col_index) = coord
        return (
            col_index >= 0 and \
            col_index < self.col_length and \
            row_index >= 0 and \
            row_index < self.row_length
        )
