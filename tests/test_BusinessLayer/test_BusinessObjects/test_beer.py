from BusinessLayer.BusinessObjects.beer import Beer
from unittest import TestCase


class TestBeer(TestCase):

    def test_create_beer(self):
        # GIVEN
        name_beer = 'Leffe'
        type_beer = 'blonde'
        # WHEN
        beer = Beer(name_beer, type_beer)
        # THEN
        self.assertIsInstance(beer, Beer)
        self.assertEqual('Leffe', beer.name_beer)
        self.assertEqual('blonde', beer.type_beer)

    def test_equal_beers(self):
        # GIVEN
        name_beer1 = 'Leffe'
        type_beer1 = 'blonde'
        name_beer2 = 'Grimbergen'
        type_beer2 = 'triple'
        # WHEN
        beer1 = Beer(name_beer1, type_beer1)
        beer2 = Beer(name_beer2, type_beer2)
        # THEN
        self.assertTrue(Beer('Leffe', 'blonde') == beer1)
        self.assertFalse(beer1 == beer2)