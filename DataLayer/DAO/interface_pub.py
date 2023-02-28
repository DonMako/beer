from abc import ABC, abstractmethod
from BusinessLayer.BusinessObjects.pub import Pub
from typing import List


class InterfacePub(ABC):
    
    @abstractmethod
    def get_pubs_city(self, city: str) -> List:
        raise NotImplementedError
    
    @abstractmethod
    def get_name_pub(self, pub: Pub) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_adress_pub(self, pub: Pub) -> str:
        raise NotImplementedError