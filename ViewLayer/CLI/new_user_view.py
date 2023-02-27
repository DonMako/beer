import BusinessLayer.LocalServices.session_service as sessionService
import BusinessLayer.LocalServices.user_service as userService
from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstractView
import ViewLayer.CLI.menu as menuView
import ViewLayer.CLI.session as session


class NewUserView(abstractView.AbstractView):
    def __init__(self) -> None:
        self.__questions = [{'type': 'input', 'name': 'id_user', 'message': 'Enter an id :'},
                            {'type': 'input', 'name': 'email_user', 'message': 'Enter a mail :'},
                            {'type': 'password', 'name': 'password_user', 'message': 'Enter a password :'},
                            {'type': 'input', 'name': 'favorite_beer_flavor', 'message': "Enter your favorite beer flavor :"},
                            {'type': 'input', 'name': 'budget_user', 'message': "Enter your budget :", 'filter': float}]

    def make_choice(self):
        answers = prompt(self.__questions)
        succes = userService.UserService().create_user(answers['id_user'], answers['email_user'], answers['password_user'], 
                                           answers['favorite_beer_flavor'], answers['budget_user'])
        if not(succes):
            print("Error")
            return NewUserView()
        session.Session().user = sessionService.SessionService().open_session(answers['id_user'], answers['password_user'])
        return menuView.MenuView()