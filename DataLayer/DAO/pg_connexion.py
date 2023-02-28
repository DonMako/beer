import DataLayer.DAO.interface_connexion as interface_connexion
import psycopg as pg
from psycopg.rows import dict_row


class PGConnexion(interface_connexion.InterfaceConnexion):

    def open_connexion(self, host, port, database, user, password):
        try:
            connexion_string = "host=" + str(host) + " port=" + str(port) + " dbname=" + str(database) +\
                               " user=" + str(user) + " password=" + str(password)
            connexion = pg.connect(conninfo=connexion_string, row_factory=dict_row, autocommit=True)
            return connexion
        except Exception as e:
            print(e)
            return None

    def close_connexion(self, connexion):
        if connexion is not None:
            connexion.close()