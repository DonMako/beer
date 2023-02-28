import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_beer as interface_beer
from typing import List


class SQLiteBeer(interface_beer.InterfaceBeer):

    def get_list_beers(self, data: dict) -> List:
        curseur = db_connexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT type_beer FROM beers WHERE name_beer=:name_beer", {"name_beer": data["name_beer"]})
        row = curseur.fetchone()
        curseur.close()
        if row is not None:
            data = dict(zip(row.keys(), row))
            data = self.__sqlite_to_dao(data)
        else:
            data = None
        return data