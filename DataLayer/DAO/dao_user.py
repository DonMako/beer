from BusinessLayer.BusinessObjects.user import User
from utils.singleton import Singleton
from hashlib import sha512


class DAOUser(metaclass=Singleton):

    @staticmethod
    def __saler_hasher_mdp(password: str) -> str:
        pwd = sha512()
        pwd.update(password.encode("utf-8"))
        return pwd.hexdigest()

    def create_user(self, infos_user: User, password: str) -> bool:
        data = infos_user.as_dict()
        data["pasword"] = self.__saler_hasher_mdp(password)
        return self.__interface.create_user(data)

    def modify_user(self, user_to_modify: User) -> bool:
        return self.__interface.modify_user(user_to_modify.as_dict())

    def delete_user(self, id_user: int) -> bool:
        return self.__interface.delete_user(id_user)

    def connexion_user(self, id: str, password: str) -> User:
        mot_de_passe_sale_hashe = self.__saler_hasher_mdp(password)
        data = self.__interface.connexion_user(id, mot_de_passe_sale_hashe)
        if data is not None:
            user = User.from_dict(data)
            return user
        raise ConnectionRefusedError