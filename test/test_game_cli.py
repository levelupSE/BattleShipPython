import unittest
from unittest.mock import call, Mock, ANY

from src.game_cli import parse_user_input, UserActionType, GameCli
from src.game import CoordStatus, CoordInfo, AttackResult, BoardLayout

class TestGameCli(unittest.TestCase):

    def test_show_returns_show_action(self):
        (action_type, action_info) = parse_user_input('show')
        self.assertEqual(action_type, UserActionType.SHOW)
        self.assertEqual(action_info, None)

    def test_coordinate_returns_attack_action_and_coordinate(self):
        (action_type, action_info) = parse_user_input('a8')
        self.assertEqual(action_type, UserActionType.ATTACK)
        expected_coordinate = ('a', '8')
        self.assertEqual(action_info, expected_coordinate)

    def test_invalid_input_returns_invalid_action(self):
        (action_type, action_info) = parse_user_input('abcde')
        self.assertEqual(action_type, UserActionType.INVALID)
        self.assertEqual(action_info, None)

    def test_exit_returns_exit_action(self):
        (action_type, action_info) = parse_user_input('exit')
        self.assertEqual(action_type, UserActionType.EXIT)
        self.assertEqual(action_info, None)

    def test_game_cli_show(self):
        game = Mock()
        view_manager = Mock()
        user_inputs = ['show']

        cli = GameCli(user_inputs, game, view_manager)

        hit = CoordInfo(CoordStatus.SHIP_HIT, 'A')
        missed = CoordInfo(CoordStatus.SHIP_MISSED, None)
        empty = CoordInfo(CoordStatus.EMPTY, None)

        coords_info = [
            [hit, missed],
            [empty, empty]
        ]
        layout = BoardLayout(coords_info, ['A', 'B'], ['1', '2'])
        game.get_board_layout_v2.return_value = layout

        cli.run()

        expected_board_text = '  1,2\nA A,x\nB  , '
        view_manager.display.assert_has_calls([call(expected_board_text), call(expected_board_text), call('Game is over')])


    def test_game_cli_attack(self):
        game = Mock()
        view_manager = Mock()
        user_inputs = ['a1']

        cli = GameCli(user_inputs, game, view_manager)

        layout = BoardLayout([], [], [])
        game.get_board_layout_v2.return_value = layout

        game.attack.return_value = AttackResult.SUCCESS
        cli.run()

        game.attack.assert_called_with('a', '1')
        view_manager.display.assert_has_calls([call('Ship hit!'), call(ANY), call('Game is over')])


    def test_invalid_input(self):
        game = Mock()
        view_manager = Mock()
        user_inputs = ['blah']

        cli = GameCli(user_inputs, game, view_manager)

        layout = BoardLayout([], [], [])
        game.get_board_layout_v2.return_value = layout
        cli.run()

        view_manager.display.assert_has_calls([call('Invalid user input'), call(ANY), call('Game is over')])
