from BusinessLayer.BusinessObjects.pub import Pub
import DataLayer.DAO.interface_factory as interface_factory
from typing import List
from utils.singleton import Singleton


class DAOPub(metaclass=Singleton):

    def __init__(self):
        self.__interface = interface_factory.InterfaceFactory.get_interface("Pub")

    def get_pubs_city(self, city: str) -> List:
        return self.__interface.get_pubs_city(city)
    
    def get_name_pub(self, pub: Pub) -> str:
        return self.__interface.get_name_pub(pub.as_dict())
    
    def get_adress_pub(self, pub: Pub) -> str:
        return self.__interface.get_adress_pub(pub.as_dict())