from typing import List
import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_menu as interface_menu


class PGMenu(interface_menu.InterfaceMenu):
    
    def get_pub_beers(self, name_pub: str) -> List:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            rows = curseur.execute("SELECT name_beer, price_beer FROM menus WHERE name_pub=(%s)", (name_pub)).fetchall()
        return rows