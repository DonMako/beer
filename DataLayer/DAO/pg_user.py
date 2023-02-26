from typing import List
from DataLayer.DAO.db_connexion import DBConnexion
from DataLayer.DAO.interface_user import InterfaceUser


class PGUser(InterfaceUser):

    def create_user(self, data: dict) -> bool:
        try:
            with DBConnexion().connexion.cursor() as curseur:
                curseur.execute("INSERT INTO users (id, password, favorite_beer_flavor, budget) VALUES((%s), (%s), (%s), (%s), (%s), (%s), (%s))",
                                (data['id'], data['password'], data['favorite_beer_flavor'], data['budget']))
            return True
        except Exception as e:
            print(e)
            return False

    def modify_user(self, data: dict) -> bool:
        try:
            with DBConnexion().connexion.cursor() as curseur:
                curseur.execute("UPDATE users SET id=(%s), password=(%s), favorite_beer_flavor=(%s), budget=(%s) WHERE id=(%s) AND password=(%s)",
                                (data['id'], data['password'], data['favorite_beer_flavor'], data['budget']))
            return True
        except Exception as e:
            print(e)
            return False
    
    def delete_user(self, id: str, password: str) -> bool:
        try:
            with DBConnexion().connexion.cursor() as curseur:
                curseur.execute("DELETE FROM users WHERE id=(%s) AND password=(%s)", (id, password,))
            return True
        except Exception as e:
            print(e)
            return False
        
    def connexion_user(self, nom_utilisateur: str, mdp_sale_hashe: str) -> dict:
        with DBConnexion().connexion.cursor() as curseur:
            row = curseur.execute("SELECT * FROM agents WHERE nom_utilisateur=(%s) AND mot_de_passe=(%s)",
                                  (nom_utilisateur, mdp_sale_hashe)).fetchone()
        return row

    def modify_id(self, id_agent: int, nom_utilisateur: str, mdp_sale_hashe: str) -> bool:
        try:
            with DBConnexion().connexion.cursor() as curseur:
                curseur.execute("""
                UPDATE agents SET nom_utilisateur=(%s), mot_de_passe=(%s)
                WHERE identifiant_agent=(%s)
                """, (nom_utilisateur, mdp_sale_hashe, id_agent))
            return True
        except Exception as e:
            print(e)
            return False

    def check_id(self, id_agent: int, nom_utilisateur: str, mdp_sale_hashe: str) -> bool:
        with DBConnexion().connexion.cursor() as curseur:
            row = curseur.execute("SELECT nom_utilisateur, mot_de_passe FROM agents WHERE identifiant_agent=(%s)",
                                  (id_agent,)).fetchone()
        return nom_utilisateur == row['nom_utilisateur'] and mdp_sale_hashe == row['mot_de_passe']

    def get_favorite_flavour(self, id_agent: int) -> float:
        with DBConnexion().connexion.cursor() as curseur:
            row = curseur.execute("SELECT quotite FROM agents WHERE identifiant_agent=(%s)", (id_agent,)).fetchone()
        data = row['quotite']
        return data