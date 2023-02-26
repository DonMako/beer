from typing import List
from DataLayer.DAO.db_connexion import DBConnexion
from DataLayer.DAO.interface_user import InterfaceUser


class SQLiteUser(InterfaceUser):

    def get_user(self, id_user: int) -> dict:
        curseur = DBConnexion().connexion.cursor()
        curseur.execute("SELECT * FROM users WHERE identifiant_user=:id", {"id": id_user})
        row = curseur.fetchone()
        curseur.close()
        data = dict(zip(row.keys(), row))
        data = self.__sqlite_to_dao(data)
        return data

    def recuperer_liste_agents(self, id_superviseur: int, agents_delegues: bool = False) -> List[dict]:
        if id_superviseur > 0:
            if not agents_delegues:
                request = "SELECT * FROM agents WHERE identifiant_superviseur =:id_superviseur"
            else:
                request = """SELECT * FROM agents
                WHERE identifiant_superviseur =:id_superviseur AND identifiant_delegue IS NOT NULL"""
        else:
            request = "SELECT * FROM agents"
        curseur = DBConnexion().connexion.cursor()
        curseur.execute(request, {"id_superviseur": id_superviseur})
        rows = curseur.fetchall()
        curseur.close()
        answer = []
        for row in rows:
            data = dict(zip(row.keys(), row))
            data = self.__sqlite_to_dao(data)
            answer.append(data)
        return answer

    def delete_user(self, id_user: int) -> bool:
        try:
            curseur = DBConnexion().connexion.cursor()
            curseur.execute("DELETE FROM users WHERE identifiant_user=:id", {"id": id_user})
            DBConnexion().connexion.commit()
            curseur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def create_user(self, data: dict) -> bool:
        data = self.__dao_to_sqlite(data)
        try:
            curseur = DBConnexion().connexion.cursor()
            curseur.execute("""
            INSERT INTO users (est_superviseur, quotite, identifiant_superviseur,nom_utilisateur, mot_de_passe, prenom, nom)
            VALUES(:est_superviseur, :quotite, :identifiant_superviseur, :nom_utilisateur, :mot_de_passe, :prenom, :nom)
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

    def connexion_user(self, name_user: str, mdp_sale_hashe: str) -> dict:
        curseur = DBConnexion().connexion.cursor()
        curseur.execute("SELECT * FROM agents WHERE nom_utilisateur=:login AND mot_de_passe=:pwd",
                        {"login": name_user, "pwd": mdp_sale_hashe})
        row = curseur.fetchone()
        curseur.close()
        if row is not None:
            data = dict(zip(row.keys(), row))
            data = self.__sqlite_to_dao(data)
        else:
            data = None
        return data

    def modifier_identifiants(self, id_agent: int, nom_utilisateur: str, mdp_sale_hashe: str) -> bool:
        try:
            curseur = DBConnexion().connexion.cursor()
            curseur.execute("""
            UPDATE agents SET nom_utilisateur=:login, mot_de_passe=:pwd
            WHERE identifiant_agent=:id
            """, {'id': id_agent, 'login': nom_utilisateur, 'pwd': mdp_sale_hashe})
            DBConnexion().connexion.commit()
            curseur.close()
            return True
        except Exception as e:
            print(e)
            return False

    def verifier_identifiants(self, id_agent: int, nom_utilisateur: str, mdp_sale_hashe: str) -> bool:
        curseur = DBConnexion().connexion.cursor()
        curseur.execute("SELECT nom_utilisateur, mot_de_passe FROM agents WHERE identifiant_agent=:id",
                        {'id': id_agent})
        row = curseur.fetchone()
        curseur.close()
        return nom_utilisateur == row['nom_utilisateur'] and mdp_sale_hashe == row['mot_de_passe']

    def recuperer_nom_utilisateur(self, id_agent: int) -> str:
        curseur = DBConnexion().connexion.cursor()
        curseur.execute("SELECT nom_utilisateur FROM agents WHERE identifiant_agent=:id", {"id": id_agent})
        row = curseur.fetchone()
        curseur.close()
        data = str(row['nom_utilisateur'])
        return data