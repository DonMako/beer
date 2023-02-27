import DataLayer.DAO.dao_pub as daoPub
from typing import List
from utils.singleton import Singleton


class PubService(metaclass=Singleton):
    
    @staticmethod
    def get_list_pubs(localisation: str) -> List:
        return daoPub.DAOPub().get_list_pubs(localisation)