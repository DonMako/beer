from BusinessLayer.BusinessObjects.user import User
from utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self):
        self.__user = None

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value: User):
        self.__user = value