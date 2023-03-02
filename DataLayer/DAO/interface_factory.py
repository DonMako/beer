import DataLayer.DAO.pg_beer as pg_beer
import DataLayer.DAO.pg_connexion as pg_connexion
import DataLayer.DAO.pg_menu as pg_menu
import DataLayer.DAO.pg_pub as pg_pub
import DataLayer.DAO.pg_user as pg_user
import DataLayer.DAO.sqlite_beer as sqlite_beer
import DataLayer.DAO.sqlite_connexion as sqlite_connexion
import DataLayer.DAO.sqlite_menu as sqlite_menu
import DataLayer.DAO.sqlite_pub as sqlite_pub
import DataLayer.DAO.sqlite_user as sqlite_user
import os
from utils.singleton import Singleton


class InterfaceFactory(metaclass=Singleton):
    @staticmethod
    def get_interface(type_dao: str):
        os.environ["BIERE_ENGINE"]="PostgreSQL"

        if os.environ["BIERE_ENGINE"] == "SQLite":
            if type_dao == "Beer":
                return sqlite_beer.SQLiteBeer()
            if type_dao == "Connexion":
                return sqlite_connexion.SQLiteConnexion()
            if type_dao == "Menu":
                return sqlite_menu.SQLiteMenu()
            if type_dao == "Pub":
                return sqlite_pub.SQLitePub()
            if type_dao == "User":
                return sqlite_user.SQLiteUser()
            raise NotImplementedError
        if os.environ["BIERE_ENGINE"] == "PostgreSQL":
            if type_dao == "Beer":
                return pg_beer.PGBeer()
            if type_dao == "Connexion":
                return pg_connexion.PGConnexion()
            if type_dao == "Menu":
                return pg_menu.PGMenu()
            if type_dao == "User":
                return pg_pub.PGPub()
            if type_dao == "User":
                return pg_user.PGUser()
            raise NotImplementedError
        raise NotImplementedError