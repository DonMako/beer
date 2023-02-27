from abc import ABC, abstractmethod


class AbstractView(ABC):

    @abstractmethod
    def make_choice(self):
        raise NotImplementedError