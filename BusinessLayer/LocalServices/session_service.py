from DataLayer.DAO.dao_user import DAOUser
from utils.singleton import Singleton
from ViewLayer.CLI.session import Session


class SessionService(metaclass=Singleton):
    @staticmethod
    def open_session(id_user, password_user):
        try:
            user = DAOUser().connexion_user(id_user, password_user)
        except ConnectionRefusedError:
            user = None
        return user

    @staticmethod
    def close_session():
        Session.clear()