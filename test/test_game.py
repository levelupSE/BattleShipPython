import unittest

from src.game import Game, AttackResult, CoordInfo, CoordStatus

class TestGame(unittest.TestCase):

    def test_game_with_unhit_ships_not_over(self):
        ship_coords = {
            (0,0): 'A',
            (0,1): 'A'
        }
        game = Game(ship_coords, 5, 5)
        self.assertFalse(game.game_over())

    def test_game_with_all_ships_hit_game_over(self):
        ship_coords = {
            (0,0): 'A',
            (0,1): 'A'
        }
        game = Game(ship_coords, 5, 5)
        game.attack('a', '1')
        game.attack('a', '2')
        self.assertTrue(game.game_over())

    def test_attacks_return_correct_result(self):
        ship_coords = {
            (0,0): 'A',
            (0,1): 'A'
        }
        game = Game(ship_coords, 5, 5)
        success = game.attack('a', '1')
        missed = game.attack('b', '1')
        out_of_bounds = game.attack('b', '100')

        self.assertEqual(success, AttackResult.SUCCESS)
        self.assertEqual(missed, AttackResult.MISSED)
        self.assertEqual(out_of_bounds, AttackResult.INVALID)

    def test_get_board_layout_with_no_hits(self):
        ship_coords = {
            (0,0): 'A',
        }
        game = Game(ship_coords, 2, 2)

        layout_without_hit = game.get_board_layout()
        empty_coord = CoordInfo(CoordStatus.EMPTY, None)
        expected_layout = [
          [empty_coord, empty_coord],
          [empty_coord, empty_coord]
        ]
        self.assertEqual(expected_layout, layout_without_hit)


    def test_get_board_layout_with_hits(self):
        ship_coords = {
            (0,0): 'A',
        }
        game = Game(ship_coords, 2, 2)

        game.attack('a', '2')
        game.attack('a', '1')

        empty_coord = CoordInfo(CoordStatus.EMPTY, None)
        hit_coord = CoordInfo(CoordStatus.SHIP_HIT, 'A')
        missed_coord = CoordInfo(CoordStatus.SHIP_MISSED, None)

        expected_layout = [
          [hit_coord, missed_coord],
          [empty_coord, empty_coord]
        ]
        layout = game.get_board_layout()
        self.assertEqual(expected_layout, layout)

    def test_attacks_return_correct_result(self):
        ship_coords = {
            (0,0): 'A',
            (0,1): 'A'
        }
        game = Game(ship_coords, 5, 5)
        success = game.attack('a', '1')
        missed = game.attack('b', '1')
        out_of_bounds = game.attack('b', '100')

        self.assertEqual(success, AttackResult.SUCCESS)
        self.assertEqual(missed, AttackResult.MISSED)
        self.assertEqual(out_of_bounds, AttackResult.INVALID)

    def test_game_with_invalid_input_throws_error(self):
        ship_coords = {
            (0,0): 'A',
            (0,1): 'A'
        }
        game = Game(ship_coords, 5, 5)
        with self.assertRaises(ValueError) as context:
            game.attack('a', 'z')


