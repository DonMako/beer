import DataLayer.DAO.dao_menu as dao_menu
from typing import List
from utils.singleton import Singleton


class MenuService(metaclass=Singleton):

    @staticmethod
    def get_pub_beers(name_pub: str) -> List:
        return dao_menu.DAOMenu().get_pub_beers(name_pub)