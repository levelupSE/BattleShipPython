import unittest

from src.game_cli import parse_user_input, UserActionType

class TestParseUserInput(unittest.TestCase):

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

