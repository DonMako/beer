from PyInquirer import prompt
from BusinessLayer.LocalServices.session_service import SessionService
from ViewLayer.CLI.abstract_view import AbstractView
from ViewLayer.CLI.menu import MenuView
from ViewLayer.CLI.session import Session
from BusinessLayer.BusinessObjects.user import User


class ConnexionView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [{'type': 'input', 'name': 'name_user', 'message': 'Username :'},
                            {'type': 'password', 'name': 'password', 'message': 'Password :'}]
        self.__error = "Incorrect username and/or password."

    def make_choice(self):
        answers = prompt(self.__questions)
        user = SessionService().open_session(answers['name_user'], answers['password'])
        if not (isinstance(user, User)):
            print(self.__error)
            return ConnexionView()
        Session().user = user
        return MenuView()