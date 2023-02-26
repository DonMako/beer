from PyInquirer import prompt
from BusinessLayer.LocalServices.session_service import SessionService
from BusinessLayer.LocalServices.user_service import UserService
from ViewLayer.CLI.abstract_view import AbstractView
from ViewLayer.CLI.menu import MenuView
from ViewLayer.CLI.session import Session


class NewUserView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [{'type': 'input', 'name': 'id', 'message': 'Id :'},
                            {'type': 'password', 'name': 'password', 'message': 'Password :'},
                            {'type': 'input', 'name': 'favorite_beer_flavor', 'message': "Favorite beer flavor :"},
                            {'type': 'input', 'name': 'budget', 'message': "Budget :"}]

    def make_choice(self):
        answers = prompt(self.__questions)
        succes = UserService().create_user(answers['id'], answers['password'], answers['favorite_beer_flavor'], answers['budget'])
        if not(succes):
            print("Error")
            return NewUserView()
        Session().user = SessionService().open_session(answers['id'], answers['password'])
        return MenuView()