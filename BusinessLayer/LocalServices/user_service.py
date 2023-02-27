from BusinessLayer.BusinessObjects.user import User
from DataLayer.DAO.dao_user import DAOUser
from utils.singleton import Singleton


class UserService(metaclass=Singleton):
    @staticmethod
    def create_user(id_user: str, mail_user: str, password_user: str, favorite_beer_flavor: str, budget_user: float) -> bool:
        data_user = {'id_user': id_user, 'mail_user': mail_user, 'password_user': password_user,
                     'favorite_beer_flavor': favorite_beer_flavor, 'budget_user': budget_user}
        new_user = User.from_dict(data_user)
        return DAOUser().create_user(new_user, id, password_user)

    @staticmethod
    def modify_user(user_to_modify: User) -> bool:
        return DAOUser().modify_user(user_to_modify)

    @staticmethod
    def delete_user(user_to_delete: int) -> bool:
        return DAOUser().delete_user(user_to_delete)