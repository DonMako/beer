from abc import ABC, abstractmethod
from typing import List


class InterfaceMenu(ABC):
    
    @abstractmethod
    def get_pub_beers(self, name_pub: str) -> List:
        raise NotImplementedError