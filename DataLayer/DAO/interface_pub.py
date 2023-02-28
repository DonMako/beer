from abc import ABC, abstractmethod
from typing import List


class InterfacePub(ABC):
    
    @abstractmethod
    def get_pubs_localisation(self, localisation: str) -> List:
        raise NotImplementedError
    
    @abstractmethod
    def get_pub_beer(self, name_pub: str) -> List:
        raise NotImplementedError