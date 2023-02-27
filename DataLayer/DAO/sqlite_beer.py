import DataLayer.DAO.db_connexion as dbConnexion
import DataLayer.DAO.interface_beer as interfaceBeer
from typing import List


class SQLiteBeer(interfaceBeer.InterfaceBeer):

    def get_list_beers(self, type_beer: str) -> List:
        curseur = dbConnexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT * FROM beers WHERE type_beer=:type_beer", {"type_beer": type_beer})
        row = curseur.fetchone()
        curseur.close()
        if row is not None:
            data = dict(zip(row.keys(), row))
            data = self.__sqlite_to_dao(data)
        else:
            data = None
        return data