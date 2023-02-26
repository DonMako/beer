from typing import List
from DataLayer.DAO.db_connexion import DBConnexion
from DataLayer.DAO.interface_user import InterfaceUser


class SQLiteUser(InterfaceUser):

    def create_user(self, data: dict) -> bool:
        data = self.__dao_to_sqlite(data)
        try:
            curseur = DBConnexion().connexion.cursor()
            curseur.execute("""
            INSERT INTO users (id, password, favorite_beer_flavor, budget)
            VALUES(:id, :password, :favorite_beer_flavor, :budget)
            """, data)
            DBConnexion().connexion.commit()
            curseur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def modify_user(self, data: dict) -> bool:
        data = self.__dao_to_sqlite(data)
        try:
            curseur = DBConnexion().connexion.cursor()
            curseur.execute("""
            UPDATE users SET est_superviseur=:est_superviseur, quotite=:quotite,
            identifiant_superviseur=:identifiant_superviseur, prenom=:prenom, nom=:nom
            WHERE identifiant_agent=:identifiant_agent
            """, data)
            DBConnexion().connexion.commit()
            curseur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_user(self, id: int, password: str) -> bool:
        try:
            curseur = DBConnexion().connexion.cursor()
            curseur.execute("DELETE FROM users WHERE id=:id AND password=:password", {"id": id, "password": password})
            DBConnexion().connexion.commit()
            curseur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def connexion_user(self, id: str, mdp_sale_hashe: str) -> dict:
        curseur = DBConnexion().connexion.cursor()
        curseur.execute("SELECT * FROM users WHERE id=:id AND password=:password", {"id": id, "password": mdp_sale_hashe})
        row = curseur.fetchone()
        curseur.close()
        if row is not None:
            data = dict(zip(row.keys(), row))
            data = self.__sqlite_to_dao(data)
        else:
            data = None
        return data