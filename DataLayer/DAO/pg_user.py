from typing import List
import DataLayer.DAO.db_connexion as dbConnexion
import DataLayer.DAO.interface_user as interfaceUser


class PGUser(interfaceUser.InterfaceUser):

    def create_user(self, data: dict) -> bool:
        try:
            with dbConnexion.DBConnexion().connexion.cursor() as curseur:
                curseur.execute("INSERT INTO users (id, email, password, favorite_beer_flavor, budget) VALUES((%s), (%s), (%s), (%s), (%s), (%s), (%s))",
                                (data['id'], data['email'], data['password'], data['favorite_beer_flavor'], data['budget']))
            return True
        except Exception as e:
            print(e)
            return False

    def modify_user(self, data: dict) -> bool:
        try:
            with dbConnexion.DBConnexion().connexion.cursor() as curseur:
                curseur.execute(
                """
                UPDATE users SET id_user=(%s), email_user=(%s), password_user=(%s), favorite_beer_flavor=(%s), budget_user=(%s) 
                WHERE id_user=(%s) AND password_user=(%s)
                """,
                (data['id_user'], data['email_user'], data['password_user'], data['favorite_beer_flavor'], data['budget_user']))
            return True
        except Exception as e:
            print(e)
            return False
    
    def delete_user(self, id_user: str, password_user: str) -> bool:
        try:
            with dbConnexion.DBConnexion().connexion.cursor() as curseur:
                curseur.execute("DELETE FROM users WHERE id_user=(%s) AND password_user=(%s)", (id_user, password_user,))
            return True
        except Exception as e:
            print(e)
            return False
        
    def connexion_user(self, id_user: str, password_sale_hashe: str) -> dict:
        with dbConnexion.DBConnexion().connexion.cursor() as curseur:
            row = curseur.execute("SELECT * FROM agents WHERE id_user=(%s) AND password_user=(%s)",
                                  (id_user, password_sale_hashe)).fetchone()
        return row