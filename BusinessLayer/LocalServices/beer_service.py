import DataLayer.DAO.dao_beer as dao_beer
from typing import List
from utils.singleton import Singleton


class BeerService(metaclass=Singleton):

    @staticmethod
    def get_list_beers(type_beer: str) -> List:
        return dao_beer.DAOBeer().get_list_beers(type_beer)