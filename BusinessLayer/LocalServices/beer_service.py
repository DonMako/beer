import DataLayer.DAO.dao_beer as dao_beer
from utils.singleton import Singleton


class BeerService(metaclass=Singleton):

    @staticmethod
    def get_type_beer(type_beer: str) -> str:
        return dao_beer.DAOBeer().get_list_beers(type_beer)
    
    @staticmethod
    def get_price_beer(type_beer: str) -> str:
        return dao_beer.DAOBeer().get_price_beer(type_beer)