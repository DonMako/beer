import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_beer as interface_beer
from typing import List


class SQLiteBeer(interface_beer.InterfaceBeer):

    def get_type_beer(self, data: dict) -> List:
        curseur = db_connexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT type_beer FROM beers WHERE name_beer=:name_beer", {"name_beer": data["name_beer"]})
        row = curseur.fetchone()
        curseur.close()
        if row is not None:
            data = dict(zip(row.keys(), row))
        else:
            data = None
        return data
    
    def get_price_beer(self, data: dict) -> List:
        curseur = db_connexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT price_beer FROM beers WHERE name_beer=:name_beer", {"name_beer": data["name_beer"]})
        row = curseur.fetchone()
        curseur.close()
        if row is not None:
            data = dict(zip(row.keys(), row))
        else:
            data = None
        return data