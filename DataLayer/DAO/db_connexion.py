import DataLayer.DAO.interface_factory as interface_factory
import os
from utils.singleton import Singleton


class DBConnexion(metaclass=Singleton):
    
    def __init__(self):
        self.__interface = interface_factory.InterfaceFactory().get_interface("Connexion")
        self.__connexion = self.__interface.open_connexion(os.environ["BIERE_HOST"],
                                                           os.environ["BIERE_PORT"],
                                                           os.environ["BIERE_DATABASE"],
                                                           os.environ["BIERE_USER"],
                                                           os.environ["BIERE_PASSWORD"])
        if self.__connexion is None:
            raise ConnectionError
        
    @property
    def connexion(self):
        return self.__connexion
    
    def __del__(self):
        self.__interface.close_connexion(self.__connexion)