from abc import ABC, abstractmethod
from typing import List


class InterfacePub(ABC):
    
    @abstractmethod
    def get_list_beers(self, localisation: str) -> List:
        raise NotImplementedError