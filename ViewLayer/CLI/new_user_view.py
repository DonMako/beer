from BusinessLayer.LocalServices.session_service import SessionService
from BusinessLayer.LocalServices.user_service import UserService
from PyInquirer import prompt
from ViewLayer.CLI.abstract_view import AbstractView
from ViewLayer.CLI.menu import MenuView
from ViewLayer.CLI.session import Session


class NewUserView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [{'type': 'input', 'name': 'id_user', 'message': 'Enter an id :'},
                            {'type': 'input', 'name': 'mail_user', 'message': 'Enter a mail :'},
                            {'type': 'password', 'name': 'password_user', 'message': 'Enter a password :'},
                            {'type': 'input', 'name': 'favorite_beer_flavor', 'message': "Enter your favorite beer flavor :"},
                            {'type': 'input', 'name': 'budget_user', 'message': "Enter your budget :", 'filter': float}]

    def make_choice(self):
        answers = prompt(self.__questions)
        succes = UserService().create_user(answers['id_user'], answers['mail_user'], answers['password_user'], 
                                           answers['favorite_beer_flavor'], answers['budget_user'])
        if not(succes):
            print("Error")
            return NewUserView()
        Session().user = SessionService().open_session(answers['id_user'], answers['password_user'])
        return MenuView()