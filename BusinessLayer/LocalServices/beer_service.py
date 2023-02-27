import DataLayer.DAO.dao_beer as daoBeer
from typing import List
from utils.singleton import Singleton


class BeerService(metaclass=Singleton):

    @staticmethod
    def get_list_beers(type_beer: str) -> List:
        return daoBeer.DAOBeer().get_list_beers(type_beer)