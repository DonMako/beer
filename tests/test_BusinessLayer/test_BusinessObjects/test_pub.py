from BusinessLayer.BusinessObjects.pub import Pub
from unittest import TestCase


class TestPub(TestCase):

    def test_create_pub(self):
        # GIVEN
        name_pub = 'Chez Lulu'
        adress_pub = '3 rue Général Rémi'
        city_pub = 'Paris'
        # WHEN
        pub = Pub(name_pub, adress_pub, city_pub)
        # THEN
        self.assertIsInstance(pub, Pub)
        self.assertEqual('Leffe', pub.name_pub)
        self.assertEqual('3 rue Général Rémi', pub.adress_pub)
        self.assertEqual('blonde', pub.city_pub)

    def test_equal_pubs(self):
        # GIVEN
        name_pub1 = 'Chez Lulu'
        adress_pub1 = '3 rue Général Rémi'
        city_pub1 = 'Paris'
        name_pub2 = 'Au bon bar'
        adress_pub2 = '17 rue Jules Lebrun'
        city_pub2 = 'Rennes'
        # WHEN
        pub1 = Pub(name_pub1, adress_pub1, city_pub1)
        pub2 = Pub(name_pub2, adress_pub2, city_pub2)
        # THEN
        self.assertTrue(Pub('Chez Lulu', '3 rue Général Rémi', 'Paris') == pub1)
        self.assertFalse(pub1 == pub2)