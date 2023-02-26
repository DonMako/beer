import sqlite3
from DataLayer.DAO.interface_connexion import InterfaceConnexion


class SQLiteConnexion(InterfaceConnexion):

    def open_connexion(self, host):
        try:
            connexion = sqlite3.connect(host)
            connexion.row_factory = sqlite3.Row
            return connexion
        except Exception as e:
            print(e)
            return None

    def close_connexion(self, connexion):
        if connexion is not None:
            connexion.close()