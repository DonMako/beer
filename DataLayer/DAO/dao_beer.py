from BusinessLayer.BusinessObjects.beer import Beer
import DataLayer.DAO.interface_factory as interface_factory
from utils.singleton import Singleton


class DAOBeer(metaclass=Singleton):

    def __init__(self):
        self.__interface = interface_factory.InterfaceFactory.get_interface("Pub")

    def get_type_beer(self, beer: Beer) -> str:
        return self.__interface.get_type_beer(beer.as_dict)