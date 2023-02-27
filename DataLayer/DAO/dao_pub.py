import DataLayer.DAO.interface_factory as interfaceFactory
from hashlib import sha512
from typing import List
from utils.singleton import Singleton


class DAOPub(metaclass=Singleton):

    def __init__(self):
        self.__interface = interfaceFactory.InterfaceFactory.get_interface("Pub")

    def get_list_pubs(self, localisation: str) -> List:
        return self.__interface.get_list_pubs(localisation)