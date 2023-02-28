import DataLayer.DAO.interface_factory as interface_factory
from typing import List
from utils.singleton import Singleton


class DAOMenu(metaclass=Singleton):

    def __init__(self):
        self.__interface = interface_factory.InterfaceFactory.get_interface("Menu")

    def get_pub_beers(self, name_pub: str) -> List:
        return self.__interface.get_pub_beers(name_pub)