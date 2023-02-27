from typing import List
import DataLayer.DAO.db_connexion as dbConnexion
import DataLayer.DAO.interface_pub as interfacePub


class PGPub(interfacePub.InterfacePub):

    def get_list_pubs(self, localisation: str) -> List:
        with dbConnexion.DBConnexion().connexion.cursor() as curseur:
            row = curseur.execute("SELECT * FROM pubs WHERE localisation_pub=(%s)", (localisation)).fetchone()
        return row