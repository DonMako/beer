import DataLayer.DAO.interface_connexion as interface_connexion
import sqlite3


class SQLiteConnexion(interface_connexion.InterfaceConnexion):

    def open_connexion(self, host, port, database, user, password):
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