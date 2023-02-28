import DataLayer.DAO.db_connexion as db_connexion
import DataLayer.DAO.interface_user as interface_user


class PGUser(interface_user.InterfaceUser):

    def create_user(self, data: dict) -> bool:
        try:
            with db_connexion.DBConnexion().connexion.cursor() as curseur:
                curseur.execute(
                """
                INSERT INTO users (id_user, email_user, password_user, favorite_beer_type, budget_user) VALUES((%s), (%s), (%s), (%s), (%s), (%s), (%s))
                """,
                (data['id_user'], data['email_user'], data['password_user'], data['favorite_beer_type'], data['budget_user']))
            return True
        except Exception as e:
            print(e)
            return False

    def modify_user(self, data: dict) -> bool:
        try:
            with db_connexion.DBConnexion().connexion.cursor() as curseur:
                curseur.execute(
                """
                UPDATE users SET id_user=(%s), email_user=(%s), password_user=(%s), favorite_beer_type=(%s), budget_user=(%s) 
                WHERE id_user=(%s) AND password_user=(%s)
                """,
                (data['id_user'], data['email_user'], data['password_user'], data['favorite_beer_type'], data['budget_user']))
            return True
        except Exception as e:
            print(e)
            return False
    
    def delete_user(self, data: dict) -> bool:
        try:
            with db_connexion.DBConnexion().connexion.cursor() as curseur:
                curseur.execute("DELETE FROM users WHERE id_user=(%s) AND password_user=(%s)", 
                                (data["id_user"], data["password_user"],))
            return True
        except Exception as e:
            print(e)
            return False
        
    def connexion_user(self, id_user: str, password_sale_hashe: str) -> dict:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            row = curseur.execute("SELECT * FROM users WHERE id_user=(%s) AND password_user=(%s)",
                                  (id_user, password_sale_hashe)).fetchone()
        return row
    
    def get_email_user(self, data: dict) -> str:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            email_user = curseur.execute("SELECT email_user FROM users WHERE id_user=(%s) AND password_user=(%s)",
                                         (data["id_user"], data["password_user"])).fetchone()
        return email_user
    
    def get_favorite_beer_type(self, data: dict) -> str:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            favorite_beer_type = curseur.execute("SELECT favorite_beer_type FROM users WHERE id_user=(%s) AND password_user=(%s)",
                                         (data["id_user"], data["password_user"])).fetchone()
        return favorite_beer_type
    
    def get_budget_user(self, data: dict) -> float:
        with db_connexion.DBConnexion().connexion.cursor() as curseur:
            budget_user = curseur.execute("SELECT budget_user FROM users WHERE id_user=(%s) AND password_user=(%s)",
                                         (data["id_user"], data["password_user"])).fetchone()
        return budget_user