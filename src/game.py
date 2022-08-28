from enum import Enum
from dataclasses import dataclass

class CoordStatus(Enum):
    '''Status of a board coordinate'''
    SHIP_HIT = 1
    SHIP_MISSED = 2
    EMPTY = 3

    def __repr__(self):
        return self.name

@dataclass
class CoordInfo:
    status: CoordStatus
    ship_name: str

    def __repr__(self):
        if self.status == CoordStatus.SHIP_HIT:
            return self.ship_name
        return self.status.name

def index_to_letter(index):
    a_int = 97
    return chr(a_int + index)

class Game:
    def __init__(self, ship_coords, col_length = 10, row_length = 10):
        self.attacked_coords = set()
        self.ship_coords = ship_coords
        self.row_length = row_length
        self.col_length = col_length

    def attack(self, row, col):
        coord = (row, col)

        # already attacked that position
        if coord in self.attacked_coords:
            return False

        self.attacked_coords.add(coord)
        return coord in self.ship_coords

    def game_over(self):
        attacked_ship_coords = self.attacked_coords.intersection(set(self.ship_coords.keys()))
        return len(attacked_ship_coords) == len(self.ship_coords)

    def get_board_layout(self):
        return [
            [self._get_coord_status(index_to_letter(row_index), str(col_index)) for row_index in range(self.row_length) ]
            for col_index in range(1, self.col_length + 1)
        ]

    def _get_coord_status(self, row, col):
        coord = (row, col)

        if coord in self.attacked_coords and coord in self.ship_coords:
            return CoordInfo(CoordStatus.SHIP_HIT, self.ship_coords[coord])

        if coord in self.attacked_coords:
            return CoordInfo(CoordStatus.SHIP_MISSED, None)

        return CoordInfo(CoordStatus.EMPTY, None)
