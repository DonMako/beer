import DataLayer.DAO.dao_pub as dao_pub
from typing import List
from utils.singleton import Singleton


class PubService(metaclass=Singleton):
    
    @staticmethod
    def get_pubs_localisation(localisation: str) -> List:
        return dao_pub.DAOPub().get_pubs_localisation(localisation)
    
    @staticmethod
    def get_pub_beer(name_pub: str) -> List:
        return dao_pub.DAOPub().get_pub_beer(name_pub)