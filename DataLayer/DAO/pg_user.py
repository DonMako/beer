from typing import List
from DataLayer.DAO.db_connexion import DBConnexion
from DataLayer.DAO.interface_user import InterfaceUser


class PGUser(InterfaceUser):

    def delete_user(self, id_agent: int) -> bool:
        try:
            with DBConnexion().connexion.cursor() as curseur:
                curseur.execute("DELETE FROM agents WHERE identifiant_agent=(%s)", (id_agent,))
            return True
        except Exception as e:
            print(e)
            return False

    def create_user(self, data: dict) -> bool:
        try:
            with DBConnexion().connexion.cursor() as curseur:
                curseur.execute("""
                INSERT INTO agents (est_superviseur, quotite, identifiant_superviseur,
                nom_utilisateur, mot_de_passe, prenom, nom)
                VALUES((%s), (%s), (%s), (%s), (%s), (%s), (%s))
                """, (data['est_superviseur'], data['quotite'], data['identifiant_superviseur'],
                      data['nom_utilisateur'], data['mot_de_passe'], data['prenom'], data['nom']))
            return True
        except Exception as e:
            print(e)
            return False

    def modify_user(self, data: dict) -> bool:
        try:
            with DBConnexion().connexion.cursor() as curseur:
                curseur.execute("""
                UPDATE agents SET est_superviseur=(%s), quotite=(%s),
                identifiant_superviseur=(%s), prenom=(%s), nom=(%s)
                WHERE identifiant_agent=(%s)
                """, (data['est_superviseur'], data['quotite'], data['identifiant_superviseur'],
                      data['prenom'], data['nom'], data['identifiant_agent']))
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