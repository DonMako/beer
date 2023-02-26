import os
import DataLayer.DAO.interface_factory as factory
from utils.singleton import Singleton



class DBConnexion(metaclass=Singleton):
    def __init__(self):
        self.__interface = factory.InterfaceFactory().get_interface("Connexion")
        self.__connexion = self.__interface.ouvrir_connexion(os.environ["PSYCOQUAC_HOST"], os.environ["PSYCOQUAC_PORT"],
                                                             os.environ["PSYCOQUAC_DATABASE"],
                                                             os.environ["PSYCOQUAC_USER"],
                                                             os.environ["PSYCOQUAC_PASSWORD"])
        if self.__connexion is None:
            raise ConnectionError

    @property
    def connexion(self):
        return self.__connexion

    def __del__(self):
        self.__interface.close_connexion(self.__connexion)
