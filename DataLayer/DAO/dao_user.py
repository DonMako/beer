from BusinessLayer.BusinessObjects.user import User
from DataLayer.DAO.interface_factory import InterfaceFactory
from hashlib import sha512
from utils.singleton import Singleton


class DAOUser(metaclass=Singleton):

    def __init__(self):
        self.__interface = InterfaceFactory.get_interface("User")

    @staticmethod
    def __saler_hasher_mdp(password_user: str) -> str:
        pwd = sha512()
        pwd.update(password_user.encode("utf-8"))
        return pwd.hexdigest()

    def create_user(self, infos_user: User, password_user: str) -> bool:
        data = infos_user.as_dict()
        data["password_user"] = self.__saler_hasher_mdp(password_user)
        return self.__interface.create_user(data)

    def modify_user(self, user_to_modify: User) -> bool:
        return self.__interface.modify_user(user_to_modify.as_dict())

    def delete_user(self, id_user: int) -> bool:
        return self.__interface.delete_user(id_user)

    def connexion_user(self, id_user: str, password_user: str) -> User:
        password_user_sale_hashe = self.__saler_hasher_mdp(password_user)
        data = self.__interface.connexion_user(id_user, password_user_sale_hashe)
        if data is not None:
            user = User.from_dict(data)
            return user
        raise ConnectionRefusedError