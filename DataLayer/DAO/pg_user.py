from typing import List
import DataLayer.DAO.db_connexion as dbConnexion
import DataLayer.DAO.interface_user as interfaceUser


class PGUser(interfaceUser.InterfaceUser):

    def create_user(self, data: dict) -> bool:
        try:
            with dbConnexion.DBConnexion().connexion.cursor() as curseur:
                curseur.execute("INSERT INTO users (id, password, favorite_beer_flavor, budget) VALUES((%s), (%s), (%s), (%s), (%s), (%s), (%s))",
                                (data['id'], data['password'], data['favorite_beer_flavor'], data['budget']))
            return True
        except Exception as e:
            print(e)
            return False

    def modify_user(self, data: dict) -> bool:
        try:
            with dbConnexion.DBConnexion().connexion.cursor() as curseur:
                curseur.execute("UPDATE users SET id=(%s), password=(%s), favorite_beer_flavor=(%s), budget=(%s) WHERE id=(%s) AND password=(%s)",
                                (data['id'], data['password'], data['favorite_beer_flavor'], data['budget']))
            return True
        except Exception as e:
            print(e)
            return False
    
    def delete_user(self, id: str, password: str) -> bool:
        try:
            with dbConnexion.DBConnexion().connexion.cursor() as curseur:
                curseur.execute("DELETE FROM users WHERE id=(%s) AND password=(%s)", (id, password,))
            return True
        except Exception as e:
            print(e)
            return False
        
    def connexion_user(self, nom_utilisateur: str, mdp_sale_hashe: str) -> dict:
        with dbConnexion.DBConnexion().connexion.cursor() as curseur:
            row = curseur.execute("SELECT * FROM agents WHERE nom_utilisateur=(%s) AND mot_de_passe=(%s)",
                                  (nom_utilisateur, mdp_sale_hashe)).fetchone()
        return row