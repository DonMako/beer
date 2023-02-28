from typing import List
import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_beer as interface_beer


class PGBeer(interface_beer.InterfaceBeer):

    def get_list_beers(self, type_beer: str) -> List:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            row = curseur.execute("SELECT * FROM beers WHERE type_beer=(%s)", (type_beer)).fetchone()
        return row