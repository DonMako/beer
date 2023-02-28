import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_pub as interface_pub
from typing import List


class SQLitePub(interface_pub.InterfacePub):

    def get_pubs_localisation(self, localisation: str) -> List:
        curseur = db_connexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT * FROM pubs WHERE localisation=:localisation", {"localisation": localisation})
        rows = curseur.fetchall()
        curseur.close()
        answer = []
        for row in rows:
            data = dict(zip(row.keys(), row))
            data = self.__sqlite_to_dao(data)
            answer.append(data)
        return answer