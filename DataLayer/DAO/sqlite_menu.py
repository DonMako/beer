import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_menu as interface_menu
from typing import List


class SQLiteMenu(interface_menu.InterfaceMenu):

    def get_pub_beers(self, name_pub: str) -> List:
            curseur = db_connexion.DBConnexion().connexion.cursor()
            curseur.execute("SELECT name_beer, price_beer FROM menus WHERE name_pub=:name_pub", {"name_pub": name_pub})
            rows = curseur.fetchall()
            curseur.close()
            answer = []
            for row in rows:
                data = dict(zip(row.keys(), row))
                data = self.__sqlite_to_dao(data)
                answer.append(data)
            return answer