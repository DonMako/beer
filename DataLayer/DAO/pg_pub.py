from typing import List
import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_pub as interface_pub


class PGPub(interface_pub.InterfacePub):

    def get_pubs_localisation(self, localisation: str) -> List:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            rows = curseur.execute("SELECT * FROM pubs WHERE localisation_pub=(%s)", (localisation)).fetchall()
        return rows
    
    def get_pub_beer(self, name_pub: str) -> List:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            rows = curseur.execute("SELECT name_beer, price_beer FROM menus WHERE name_pub=(%s)", (name_pub)).fetchall()
        return rows