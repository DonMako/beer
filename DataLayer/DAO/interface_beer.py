from abc import ABC, abstractmethod
from BusinessLayer.BusinessObjects.beer import Beer


class InterfaceBeer(ABC):
    
    @abstractmethod
    def get_type_beer(self, beer: Beer) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_price_beer(self, beer: Beer) -> str:
        raise NotImplementedError