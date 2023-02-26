from BusinessLayer.BusinessObjects.user import User
from utils.singleton import Singleton
from hashlib import sha512


class DAOUser(metaclass=Singleton):

    @staticmethod
    def __saler_hasher_mdp(id: str, password: str) -> str:
        pwd = sha512()
        pwd.update(id.encode("utf-8"))
        pwd.update(password.encode("utf-8"))
        return pwd.hexdigest()

    def get_user(self, id_user: int) -> User:
        data = self.__interface.get_user(id_user)
        return User.from_dict(data)

    def create_user(self, infos_user: User, id: str, password: str) -> bool:
        data = infos_user.as_dict()
        if data['est_superviseur'] and data['identifiant_superviseur'] is None:
            data['identifiant_superviseur'] = self.__interface.recuperer_dernier_id_agent() + 1
        data["id"] = id
        data["mot_de_passe"] = self.__saler_hasher_mdp(id, password)
        return self.__interface.create_user(data)

    def modify_user(self, user_to_modify: User) -> bool:
        return self.__interface.modify_user(user_to_modify.as_dict())

    def delete_user(self, id_user: int) -> bool:
        return self.__interface.delete_user(id_user)

    def connexion_user(self, name_user: str, password: str) -> User:
        mot_de_passe_sale_hashe = self.__saler_hasher_mdp(name_user, password)
        data = self.__interface.connexion_user(name_user, mot_de_passe_sale_hashe)
        if data is not None:
            agent = User.from_dict(data)
            return agent
        raise ConnectionRefusedError

    def modify_id(self, id_user: int, name_user: str, mot_de_passe_en_clair: str) -> bool:
        mdp_sale_hashe = self.__saler_hasher_mdp(name_user, mot_de_passe_en_clair)
        res = self.__interface.modify_id(id_user, name_user, mdp_sale_hashe)
        return res

    def check_id(self, id_user: int, name_user: str, mot_de_passe_en_clair: str) -> bool:
        mdp_sale_hashe = self.__saler_hasher_mdp(name_user, mot_de_passe_en_clair)
        res = self.__interface.check_id(id_user, name_user, mdp_sale_hashe)
        return res

    def recuperer_quotite(self, id_user: int) -> float:
        return self.__interface.recuperer_quotite(id_user)

    def get_name_user(self, id_user: int) -> str:
        return self.__interface.get_name_user(id_user)