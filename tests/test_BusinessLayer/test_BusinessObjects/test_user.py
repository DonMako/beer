from BusinessLayer.BusinessObjects.user import User
from unittest import TestCase


class TestUser(TestCase):

    def test_create_user(self):
        # GIVEN
        id_example = 'toto'
        email_example = 'toto@mail.com'
        password_example = '9520df6412dfdf'
        favorite_beer_type_example = 'Blonde'
        favorite_beer_name_example = 'Leffe'        
        budget_example = 90.00
        # WHEN
        user = User(id_example, email_example, password_example, favorite_beer_type_example, favorite_beer_name_example, budget_example)
        # THEN
        self.assertIsInstance(user, User)
        self.assertEqual('toto', user.id_user)
        self.assertEqual('toto@mail.com', user.email_user)
        self.assertEqual('9520df6412dfdf', user.password_user)
        self.assertEqual('Blonde', user.favorite_beer_type)
        self.assertEqual('Leffe', user.favorite_beer_name)
        self.assertEqual(90.00, user.budget_user)

    def test_equal_users(self):
        # GIVEN
        user1_id = 'toto'
        user1_email = 'toto@mail.com'
        user1_password = "df54eq65g4zq6ffjzefz"
        user1_favorite_beer_type = 'Blonde'
        user1_favorite_beer_name = 'Leffe'
        user1_budget = 2.50
        user2_id = 'tata'
        user2_email = 'tata@mail.com'
        user2_password = "zfhi5557"
        user2_favorite_beer_type = 'Triple'
        user2_favorite_beer_name = 'Grimbergen'
        user2_budget = 37.64
        # WHEN
        user1 = User(user1_id, user1_email, user1_password, user1_favorite_beer_type, user1_favorite_beer_name, user1_budget)
        user2 = User(user2_id, user2_email, user2_password, user2_favorite_beer_type, user2_favorite_beer_name, user2_budget)
        # THEN
        self.assertTrue(User('toto', 'toto@mail.com', "df54eq65g4zq6ffjzefz", 'Blonde', 'Leffe', 2.50) == user1)
        self.assertFalse(user1 == user2)