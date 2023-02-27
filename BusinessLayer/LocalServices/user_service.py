from BusinessLayer.BusinessObjects.user import User
from DataLayer.DAO.dao_user import DAOUser
from utils.singleton import Singleton


class UserService(metaclass=Singleton):
    @staticmethod
    def create_user(id: str, mail: str, password: str, favorite_beer_flavor: str, budget: float) -> bool:
        data_user = {'id': id, 'mail': mail, 'password': password, 'favorite_beer_flavor': favorite_beer_flavor, 'budget': budget}
        new_user = User.from_dict(data_user)
        return DAOUser().create_user(new_user, id, password)

    @staticmethod
    def modify_user(user_to_modify: User) -> bool:
        return DAOUser().modify_user(user_to_modify)

    @staticmethod
    def delete_user(user_to_delete: int) -> bool:
        return DAOUser().delete_user(user_to_delete)