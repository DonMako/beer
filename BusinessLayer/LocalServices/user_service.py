from BusinessLayer.BusinessObjects.user import User
import DataLayer.DAO.dao_user as daoUser
from utils.singleton import Singleton


class UserService(metaclass=Singleton):
    
    @staticmethod
    def create_user(id_user: str, email_user: str, password_user: str, favorite_beer_type: str, budget_user: float) -> bool:
        data_user = {'id_user': id_user, 'email_user': email_user, 'password_user': password_user,
                     'favorite_beer_type': favorite_beer_type, 'budget_user': budget_user}
        new_user = User.from_dict(data_user)
        return daoUser.DAOUser().create_user(new_user, id_user, password_user)

    @staticmethod
    def modify_user(user_to_modify: User) -> bool:
        return daoUser.DAOUser().modify_user(user_to_modify)

    @staticmethod
    def delete_user(user_to_delete: User) -> bool:
        return daoUser.DAOUser().delete_user(user_to_delete)
    
    @staticmethod
    def get_email_user(user: User) -> str:
        return daoUser.DAOUser().get_email_user(user)