from BusinessLayer.BusinessObjects.user import User
from unittest import TestCase


class TestUser(TestCase):

    def test_create_user(self):
        # GIVEN
        id_example = 'toto'
        email_example = 'toto@mail.com'
        password_example = '9520df6412dfdf'
        favorite_beer_flavor_example = 'bière blonde'
        budget_example = 90.00
        # WHEN
        user = User(id_example, email_example, password_example, favorite_beer_flavor_example, budget_example)
        # THEN
        self.assertIsInstance(user, User)
        self.assertEqual('toto', user.id_user)
        self.assertEqual('toto@mail.com', user.email_user)
        self.assertEqual('9520df6412dfdf', user.password_user)
        self.assertEqual('bière blonde', user.favorite_beer_flavor)
        self.assertEqual(90.00, user.budget_user)

    def test_equal_users(self):
        # GIVEN
        user1_id = 'toto'
        user1_email = 'toto@mail.com'
        user1_password = "df54eq65g4zq6ffjzefz"
        user1_favorite_beer_flavor = 'bière ambrée'
        user1_budget = 2.50
        user2_id = 'tata'
        user2_email = 'tata@mail.com'
        user2_password = "zfhi5557"
        user2_favorite_beer_flavor = 'triple'
        user2_budget = 37.64
        # WHEN
        user1 = User(user1_id, user1_email, user1_password, user1_favorite_beer_flavor, user1_budget)
        user2 = User(user2_id, user2_email, user2_password, user2_favorite_beer_flavor, user2_budget)
        # THEN
        self.assertTrue(User('toto', 'toto@mail.com', "df54eq65g4zq6ffjzefz", 'bière ambrée', 2.50) == user1)
        self.assertFalse(user1 == user2)