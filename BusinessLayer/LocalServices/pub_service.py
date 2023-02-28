from BusinessLayer.BusinessObjects.pub import Pub
import DataLayer.DAO.dao_pub as dao_pub
from typing import List
from utils.singleton import Singleton


class PubService(metaclass=Singleton):
    
    @staticmethod
    def get_pubs_city(city: str) -> List:
        return dao_pub.DAOPub().get_pubs_city(city)
    
    @staticmethod
    def get_name_pub(pub: Pub) -> str:
        return dao_pub.DAOPub().get_name_pub(pub)
    
    @staticmethod
    def get_adress_pub(pub: Pub) -> str:
        return dao_pub.DAOPub().get_adress_pub(pub)