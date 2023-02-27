from abc import ABC, abstractmethod


class InterfaceConnexion(ABC):
    @abstractmethod
    def open_connexion(self, host, port, database, user, password):
        raise NotImplementedError

    @abstractmethod
    def close_connexion(self, connexion):
        raise NotImplementedError