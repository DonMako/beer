from typing import List
import DataLayer.DAO.db_connexion as dbConnexion
import DataLayer.DAO.interface_beer as interfaceBeer


class PGBeer(interfaceBeer.InterfaceBeer):

    def get_list_beers(self, type_beer: str) -> List:
        with dbConnexion.DBConnexion().connexion.cursor() as curseur:
            row = curseur.execute("SELECT * FROM beers WHERE type_beer=(%s)", (type_beer)).fetchone()
        return row