from DataLayer.DAO.dao_user import DAOUser
from ViewLayer.CLI.session import Session
from utils.singleton import Singleton


class SessionService(metaclass=Singleton):
    @staticmethod
    def open_session(name_user, password):
        try:
            user = DAOUser().connexion_user(name_user, password)
        except ConnectionRefusedError:
            user = None
        return user

    @staticmethod
    def close_session():
        Session.clear()