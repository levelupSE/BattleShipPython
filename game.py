
import re
from enum import Enum


class UserActionType(Enum):
    '''Different type of actions a user can perform.'''
    INVALID = 1
    SHOW = 2
    ATTACK = 3

class GameCli:
    '''Manages interactions between the user and the game.'''

    # user term to display the game board
    show = 'show'
    # starts with a letter and ends with a number
    valid_attack_pattern = r'(^[a-z]{1})([0-9]$)'

    def __init__(self, user_inputs):
        self.user_inputs = user_inputs

    def run(self):
        '''Parses and applies user provided commands to the game'''
        for user_input in self.user_inputs:
            (action_type, action_info) = self._parse_user_input(user_input)

            if action_type == UserActionType.SHOW:
                self._display_board_layout()
            elif action_type == UserActionType.ATTACK:
                (col, row) = action_info
                self._attack(col, row)
            else:
                self._display_invalid_user_input_message()

    def _parse_user_input(self, raw_user_input):
        user_input = raw_user_input.lower().strip()

        if user_input == self.show:
            return (UserActionType.SHOW, None)

        match = re.search(self.valid_attack_pattern, user_input)
        if match and match.lastindex == 2:
            col = match.group(1)
            row = match.group(2)
            return (UserActionType.ATTACK, (col, row))

        return (UserActionType.INVALID, None)


    def _display_board_layout(self):
        print('TODO: display board')

    def _attack(self, col, row):
        print('TODO: attack')

    def _display_invalid_user_input_message(self):
        print('TODO: display invalid message')

