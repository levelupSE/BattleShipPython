
import re
from enum import Enum


class UserActionType(Enum):
    '''Different type of actions a user can perform.'''
    INVALID = 1
    SHOW = 2
    ATTACK = 3


def parse_user_input(raw_user_input):
    # user term to display the game board
    show = 'show'
    # starts with a letter and ends with a number
    valid_attack_pattern = r'(^[a-z]{1})([0-9]$)'

    user_input = raw_user_input.lower().strip()

    if user_input == show:
        return (UserActionType.SHOW, None)

    match = re.search(valid_attack_pattern, user_input)
    if match and match.lastindex == 2:
        row = match.group(1)
        col = match.group(2)
        return (UserActionType.ATTACK, (row, col))

    return (UserActionType.INVALID, None)


class GameCli:
    '''Manages interactions between the user and the game.'''

    def __init__(self, user_inputs, game):
        self.user_inputs = user_inputs
        self.game = game

    def run(self):
        '''Parses and applies user provided commands to the game'''
        for user_input in self.user_inputs:
            (action_type, action_info) = parse_user_input(user_input)

            if action_type == UserActionType.SHOW:
                self._display_board_layout()
            elif action_type == UserActionType.ATTACK:
                (row, col) = action_info
                self._attack(row, col)
            else:
                self._display_invalid_user_input_message()

            if self.game.game_over():
                break

        self._display_board_layout()
        print('Game is over')


    def _display_board_layout(self):
        board = self.game.get_board_layout()
        for row in board:
            print(row)

    def _attack(self, row, col):
        hit = self.game.attack(row, col)
        if hit:
            print('Ship hit!')
        else:
            print('Ship missed!')

    def _display_invalid_user_input_message(self):
        print('TODO: display invalid message')

