import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_pub as interface_pub
from typing import List


class SQLitePub(interface_pub.InterfacePub):

    def get_pubs_city(self, city: str) -> List:
        curseur = db_connexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT * FROM pubs WHERE city_pub=:city", {"city": city})
        rows = curseur.fetchall()
        curseur.close()
        answer = []
        for row in rows:
            data = dict(zip(row.keys(), row))
            answer.append(data)
        return answer
    
    def get_name_pub(self, data: dict) -> str:
        curseur = db_connexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT name_pub FROM pubs WHERE name_pub=:name_pub", data)
        result = curseur.fetchone()
        curseur.close()
        if result is not None:
            name_pub = result
        else:
            name_pub = None
        return name_pub
    
    def get_adress_pub(self, data: dict) -> str:
        curseur = db_connexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT adress_pub FROM pubs WHERE name_pub=:name_pub", data)
        result = curseur.fetchone()
        curseur.close()
        if result is not None:
            adress_pub = result
        else:
            adress_pub = None
        return adress_pub