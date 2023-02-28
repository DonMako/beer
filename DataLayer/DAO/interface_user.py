from abc import ABC, abstractmethod


class InterfaceUser(ABC):
    
    @abstractmethod
    def create_user(self, data: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    def modify_user(self, data: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, data: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    def connexion_user(self, id_user: str, password_sale_hashe: str) -> dict:
        raise NotImplementedError
    
    @abstractmethod
    def get_email_user(self, data: dict) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_favorite_beer_type(self, data: dict) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_budget_user(self, data: dict) -> float:
        raise NotImplementedError