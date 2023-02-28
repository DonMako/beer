from typing import List
import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_beer as interface_beer


class PGBeer(interface_beer.InterfaceBeer):

    def get_type_beer(self, data: dict) -> str:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            row = curseur.execute("SELECT type_beer FROM beers WHERE name_beer=(%s)", (data)).fetchone()
        return row