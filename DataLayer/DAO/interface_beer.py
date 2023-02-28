from abc import ABC, abstractmethod
from BusinessLayer.BusinessObjects.beer import Beer


class InterfacePub(ABC):
    
    @abstractmethod
    def get_type_beer(self, beer: Beer) -> str:
        raise NotImplementedError