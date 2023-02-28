import DataLayer.DAO.dao_user as dao_user
from utils.singleton import Singleton
import ViewLayer.CLI.session as session


class SessionService(metaclass=Singleton):
    
    @staticmethod
    def open_session(id_user, password_user):
        try:
            user = dao_user.DAOUser().connexion_user(id_user, password_user)
        except ConnectionRefusedError:
            user = None
        return user

    @staticmethod
    def close_session():
        session.Session.clear()