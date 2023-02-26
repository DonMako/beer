from abc import ABC, abstractmethod


class InterfaceUser(ABC):
    @abstractmethod
    def get_user(self, id_user: int) -> dict:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, id_user: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def create_user(self, data: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    def modify_user(self, data: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    def modify_id(self, id_user: int, name_user: str, mdp_sale_hashe: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def check_id(self, id_user: int, name_user: str, mdp_sale_hashe: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    def connexion_user(self, name_user: str, mdp_sale_hashe: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_favorite_type(self, id_agent: int) -> float:
        raise NotImplementedError

    @abstractmethod
    def get_user_name(self, id_user: int) -> str:
        raise NotImplementedError
    