import os
import DataLayer.DAO.sqlite_beer as sqlite_beer
import DataLayer.DAO.sqlite_connexion as sqlite_connexion
import DataLayer.DAO.sqlite_user as sqlite_user
import DataLayer.DAO.pg_connexion as pg_connexion
import DataLayer.DAO.pg_beer as pg_beer
import DataLayer.DAO.pg_user as pg_user
from utils.singleton import Singleton


class InterfaceFactory(metaclass=Singleton):
    @staticmethod
    def get_interface(type_dao: str):
        if os.environ["BIERE_ENGINE"] == "SQLite":
            if type_dao == "Beer":
                return sqlite_beer.SQLiteBeer()
            if type_dao == "Connexion":
                return sqlite_connexion.SQLiteConnexion()
            if type_dao == "User":
                return sqlite_user.SQLiteUser()
            raise NotImplementedError
        if os.environ["BIERE_ENGINE"] == "PostgreSQL":
            if type_dao == "Beer":
                return sqlite_beer.PGBeer()
            if type_dao == "Connexion":
                return pg_connexion.PGConnexion()
            if type_dao == "User":
                return pg_user.PGUser()
            raise NotImplementedError
        raise NotImplementedError