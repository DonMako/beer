from abc import ABC, abstractmethod
from BusinessLayer.BusinessObjects.pub import Pub
from typing import List


class InterfacePub(ABC):
    
    @abstractmethod
    def get_pubs_localisation(self, localisation: str) -> List:
        raise NotImplementedError
    
    @abstractmethod
    def get_name_pub(self, pub: Pub) -> List:
        raise NotImplementedError