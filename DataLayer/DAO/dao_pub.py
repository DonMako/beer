import DataLayer.DAO.interface_factory as interface_factory
from hashlib import sha512
from typing import List
from utils.singleton import Singleton


class DAOPub(metaclass=Singleton):

    def __init__(self):
        self.__interface = interface_factory.InterfaceFactory.get_interface("Pub")

    def get_pubs_localisation(self, localisation: str) -> List:
        return self.__interface.get_pubs_localisation(localisation)
    
    def get_pub_beer(self, name_pub: str) -> List:
        return self.__interface.get_pub_beer(name_pub)