from unittest import TestCase
from BusinessLayer.BusinessObjects.user import User


class TestUser(TestCase):

    def test_create_user(self):
        # GIVEN
        user_id = 'toto'
        user_password = '9520df6412dfdf'
        user_favorite_beer_flavor = 'bière blonde'
        user_budget = 90.00
        # WHEN
        user = User(user_id, user_password, user_favorite_beer_flavor, user_budget)
        id = user.id
        password = user.password
        favorite_beer_flavor = user.cp
        budget = user.ville
        # THEN
        self.assertIsInstance(user, User)
        self.assertEqual('toto', id)
        self.assertEqual('9520df6412dfdf', password)
        self.assertEqual('bière blonde', favorite_beer_flavor)
        self.assertEqual(90.00, budget)

    def test_equal_users(self):
        # GIVEN
        user1_id = 'toto'
        user1_password = "df54eq65g4zq6ffjzefz"
        user1_favorite_beer_flavor = 'bière ambrée'
        user1_budget = 2.50
        user2_id = 'tata'
        user2_password = "zfhi5557"
        user2_favorite_beer_flavor = 'triple'
        user2_budget = 37.64
        # WHEN
        user1 = User(user1_id, user1_password, user1_favorite_beer_flavor, user1_budget)
        user2 = User(user2_id, user2_password, user2_favorite_beer_flavor, user2_budget)
        # THEN
        self.assertTrue(User('toto', "df54eq65g4zq6ffjzefz", 'bière ambrée', 2.50) == user1)
        self.assertFalse(user1 == user2)