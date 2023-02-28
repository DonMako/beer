import DataLayer.DAO.interface_factory as interface_factory
from typing import List
from utils.singleton import Singleton


class DAOPub(metaclass=Singleton):

    def __init__(self):
        self.__interface = interface_factory.InterfaceFactory.get_interface("Pub")

    def get_pubs_localisation(self, localisation: str) -> List:
        return self.__interface.get_pubs_localisation(localisation)
    
    def get_name_pub(self, name_pub: str) -> List:
        return self.__interface.get_name_pub(name_pub)