import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_pub as interface_pub
from typing import List


class PGPub(interface_pub.InterfacePub):

    def get_pubs_localisation(self, localisation: str) -> List:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            rows = curseur.execute("SELECT * FROM pubs WHERE localisation_pub=(%s)", (localisation)).fetchall()
        return rows
    
    def get_name_pub(self, data: dict) -> List:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            rows = curseur.execute("SELECT name_pub FROM pubs WHERE name_pub=(%s)", (data)).fetchall()
        return rows