import unittest
from unittest.mock import Mock

from src.ship_placer import ShipPlacer, get_valid_ship_placements

class TestShipPlacer(unittest.TestCase):

    def test_ship_too_large_cannot_be_placed(self):
        config = {
            'columns': 1,
            'rows': 1,
            'ships': [
                {'name': 'B', 'length': 2},
            ]
        }
        placer = ShipPlacer(config['ships'], config['rows'], config['columns'], {})

        with self.assertRaises(Exception) as context:
            ship_coords  = placer.build_ship_coords()

    def test_placed_ships_position_matches_ship_sizes(self):
        config = {
            'columns': 10,
            'rows': 10,
            'ships': [
                {'name': 'A', 'length': 3},
                {'name': 'B', 'length': 3},
                {'name': 'C', 'length': 3},
            ]
        }
        for i in range(100):
            placer = ShipPlacer(config['ships'], config['rows'], config['columns'], {})
            ship_coords = placer.build_ship_coords()
            expected_coords = sum([ship_config['length'] for ship_config in config['ships']])
            self.assertEqual(expected_coords, len(ship_coords))

    def test_no_valid_placements_throws_exception(self):
        config = {
            'columns': 5,
            'rows': 5,
            'ships': [
                {'name': 'B', 'length': 2},
            ]
        }
        placement_fn = lambda x, y, z: None
        placer = ShipPlacer(config['ships'], config['rows'], config['columns'], {}, placement_fn)

        with self.assertRaises(Exception) as context:
            ship_coords  = placer.build_ship_coords()


    def test_valid_placment_sets_coordinates(self):
        config = {
            'columns': 5,
            'rows': 5,
            'ships': [
                {'name': 'B', 'length': 2},
                {'name': 'C', 'length': 2}
            ]
        }

        def placement(*args, **kwargs):
            ship_config = args[1]
            if ship_config['name'] == 'B':
                yield [(0,1), (0,2)]
            elif ship_config['name'] == 'C':
                yield [(2,4), (3,4)]

        placement_fn = Mock(side_effect=placement)

        placer = ShipPlacer(config['ships'], config['rows'], config['columns'], {}, placement_fn)
        ship_coords  = placer.build_ship_coords()

        self.assertTrue(ship_coords[('a', '2')], 'B')
        self.assertTrue(ship_coords[('a', '3')], 'B')
        self.assertTrue(ship_coords[('c', '5')], 'C')
        self.assertTrue(ship_coords[('d', '5')], 'C')

    def test_get_valid_ship_placements(self):
        ship_coords = {
            (0, 0): 'B',
            (0, 1): 'B',
        }
        ship_config = {'name': 'C', 'length': 2}
        placements = list(get_valid_ship_placements(ship_coords, ship_config, 2, 2))

        self.assertTrue(len(placements) > 1)

        # currently not deduping based on where we first placed the ship
        placement = placements[0]

        # ship can only be placed in the following cooords
        self.assertTrue((1,0) in placement)
        self.assertTrue((1,1) in placement)
