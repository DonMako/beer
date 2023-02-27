import DataLayer.DAO.db_connexion as dbConnexion
import DataLayer.DAO.interface_pub as interfacePub
from typing import List


class SQLitePub(interfacePub.InterfacePub):

    def get_list_pubs(self, localisation: str) -> List:
        curseur = dbConnexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT * FROM pubs WHERE localisation=:localisation", {"localisation": localisation})
        row = curseur.fetchone()
        curseur.close()
        if row is not None:
            data = dict(zip(row.keys(), row))
            data = self.__sqlite_to_dao(data)
        else:
            data = None
        return data