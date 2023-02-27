import DataLayer.DAO.db_connexion as dbConnexion
import DataLayer.DAO.interface_user as interfaceUser


class SQLiteUser(interfaceUser.InterfaceUser):

    def create_user(self, data: dict) -> bool:
        try:
            curseur = dbConnexion.DBConnexion().connexion.cursor()
            curseur.execute(
            """
            INSERT INTO users (id_user, email_user, password_user, favorite_beer_type, budget_user)
            VALUES(:id_user, :email_user, :password_user, :favorite_beer_type, :budget_user)
            """, data)
            dbConnexion.DBConnexion().connexion.commit()
            curseur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def modify_user(self, data: dict) -> bool:
        try:
            curseur = dbConnexion.DBConnexion().connexion.cursor()
            curseur.execute(
            """
            UPDATE users SET id_user=:id_user, email_user=:email_user, password_user=:password_user,
                             favorite_beer_type=:favorite_beer_type, budget_user=:budget_user 
            WHERE id_user=:id_user, password_user=:password_user
            """, data)
            dbConnexion.DBConnexion().connexion.commit()
            curseur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_user(self, data: dict) -> bool:
        try:
            curseur = dbConnexion.DBConnexion().connexion.cursor()
            curseur.execute("DELETE FROM users WHERE id_user=:id_user, password_user=:password_user", data)
            dbConnexion.DBConnexion().connexion.commit()
            curseur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def connexion_user(self, id_user: str, password_sale_hashe: str) -> dict:
        curseur = dbConnexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT * FROM users WHERE id_user=:id_user, password_user=:password_user",
                        {"id_user": id_user, "password_user": password_sale_hashe})
        row = curseur.fetchone()
        curseur.close()
        if row is not None:
            data = dict(zip(row.keys(), row))
            data = self.__sqlite_to_dao(data)
        else:
            data = None
        return data
    
    def get_email_user(self, data: dict) -> str:
        curseur = dbConnexion.DBConnexion().connexion.cursor()
        curseur.execute("SELECT email_user FROM users WHERE id_user=:id_user, password_user=:password_user", data)
        result = curseur.fetchone()
        curseur.close()
        if result is not None:
            email_user = result
        else:
            email_user = None
        return email_user