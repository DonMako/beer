from abc import ABC, abstractmethod
from typing import List


class InterfacePub(ABC):
    
    @abstractmethod
    def get_list_pubs(self, localisation: str) -> List:
        raise NotImplementedError