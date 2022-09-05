
import re
from enum import Enum
from src.game import AttackResult


class UserActionType(Enum):
    '''Different type of actions a user can perform.'''
    INVALID = 1
    SHOW = 2
    ATTACK = 3
    EXIT = 4


def parse_user_input(raw_user_input):
    # user term to display the game board
    show = 'show'
    # user term to end game
    exit = 'exit'
    # starts with a letter and ends with numbers
    valid_attack_pattern = r'(^[a-z]{1})([0-9]+$)'

    user_input = raw_user_input.lower().strip()

    if user_input == show:
        return (UserActionType.SHOW, None)

    if user_input == exit:
        return (UserActionType.EXIT, None)

    match = re.search(valid_attack_pattern, user_input)
    if match and match.lastindex == 2:
        row = match.group(1)
        col = match.group(2)
        return (UserActionType.ATTACK, (row, col))

    return (UserActionType.INVALID, None)


class GameCli:
    '''Manages interactions between the user and the game.'''

    def __init__(self, user_inputs, game, view_manager):
        self.user_inputs = user_inputs
        self.game = game
        self.view_manager = view_manager


    def run(self):
        '''Parses and applies user provided commands to the game'''
        for user_input in self.user_inputs:
            (action_type, action_info) = parse_user_input(user_input)

            self.view_manager.clear()
            if action_type == UserActionType.SHOW:
                self._display_board_layout()
            elif action_type == UserActionType.ATTACK:
                (row, col) = action_info
                self._attack(row, col)
            elif action_type == UserActionType.EXIT:
                self.view_manager.display('Ending game')
                return
            else:
                self._display_invalid_user_input_message()

            if self.game.game_over():
                break

        self._display_board_layout()
        self.view_manager.display('Game is over')


    def _display_board_layout(self):
        board_v2 = self.game.get_board_layout_v2()

        col_header = '  ' + ','.join(board_v2.column_labels) + '\n'
        rows = '\n'.join([ board_v2.row_labels[idx] + ' ' + ','.join([str(coord) for coord in row]) for idx, row in enumerate(board_v2.coord_info)])
        self.view_manager.display(col_header + rows)

    def _attack(self, row, col):
        result = self.game.attack(row, col)
        if result == AttackResult.SUCCESS:
            self.view_manager.display('Ship hit!')
        elif result == AttackResult.MISSED:
            self.view_manager.display('Ship missed!')
        elif result == AttackResult.INVALID:
            self.view_manager.display('Invalid coordinates!')
        else:
            raise Exception('There is an unhandled attack type')

    def _display_invalid_user_input_message(self):
        self.view_manager.display('Invalid user input')

