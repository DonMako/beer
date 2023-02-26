from BusinessLayer.BusinessObjects.user import User
from DataLayer.DAO.dao_user import DAOUser
from utils.singleton import Singleton
from typing import List


class UserService(metaclass=Singleton):
    @staticmethod
    def create_user(quotite: float, nom_utilisateur: str,mot_de_passe: str, prenom: str, nom: str) -> bool:
        data_agent = {'prenom': prenom, 'nom': nom, 'quotite': quotite,'identifiant_agent': DAOUser().recuperer_dernier_id_agent() + 1}
        nouvel_agent = agent_factory.AgentFactory.from_dict(data_agent)
        return DAOUser().create_user(nouvel_agent, nom_utilisateur, mot_de_passe)

    @staticmethod
    def modifier_agent(agent_a_modifier: User) -> bool:
        return DAOUser().modifier_agent(agent_a_modifier)

    @staticmethod
    def reinitialiser_identifiants(id_agent: int, nouveau_mot_de_passe_en_clair: str,nouveau_nom_utilisateur: str = None) -> bool:
        if nouveau_nom_utilisateur is None:
            nouveau_nom_utilisateur = DAOUser().recuperer_nom_utilisateur(id_agent)
        res = DAOUser().modifier_identifiants(id_agent, nouveau_nom_utilisateur,
                                               nouveau_mot_de_passe_en_clair)
        return res

    @staticmethod
    def changer_identifiants(id_agent: int, nom_utilisateur_actuel: str,
                             mot_de_passe_actuel_en_clair: str,
                             nouveau_nom_utilisateur: str = None,
                             nouveau_mot_de_passe_en_clair: str = None) -> bool:
        validation_identifiants = DAOUser().verifier_identifiants(id_agent, nom_utilisateur_actuel,mot_de_passe_actuel_en_clair)
        if validation_identifiants:
            if nouveau_nom_utilisateur is None:
                nouveau_nom_utilisateur = nom_utilisateur_actuel
            if nouveau_mot_de_passe_en_clair is None:
                nouveau_mot_de_passe_en_clair = mot_de_passe_actuel_en_clair
            return DAOUser().modifier_identifiants(id_agent, nouveau_nom_utilisateur, nouveau_mot_de_passe_en_clair)
        return False

    @staticmethod
    def supprimer_agent(agent_a_supprimer: int) -> bool:
        pot_agent = DAOFicheAdresse().recuperer_pot(agent_a_supprimer)
        liste_id_pot = []
        for fiche in pot_agent:
            liste_id_pot.append(fiche.fiche_id)
        id_superviseur = DAOUser().recuperer_id_superviseur(agent_a_supprimer)
        if len(liste_id_pot) > 0:
            res_reaffect = DAOFicheAdresse().affecter_fiches_adresse(id_superviseur, '', liste_id_pot)
        else:
            res_reaffect = True
        res_suppr = False
        if res_reaffect:
            res_suppr = DAOUser().supprimer_agent(agent_a_supprimer)
        return res_reaffect and res_suppr

    @staticmethod
    def recuperer_id_superviseur(id_agent: int) -> int:
        """
        Cette méthode permet de récupérer l'identifiant, dans la base de données Agents, du superviseur 
        de l'agent dont on renseigne l'identifiant de la base de données Agents.
        :param id_agent:
        l'identifiant, dans la base de données Agents, de l'agent dont on cherche à récupérer l'identifiant du superviseur
        :return:
        renvoie l'identifiant, dans la base de données Agents, du superviseur de l'équipe de l'agent
        """
        return DAOUser().recuperer_id_superviseur(id_agent)

    @staticmethod
    def recuperer_agent(id_agent: int) -> Agent:
        return DAOUser().recuperer_agent(id_agent)