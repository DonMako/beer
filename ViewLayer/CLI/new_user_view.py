import BusinessLayer.LocalServices.session_service as session_service
import BusinessLayer.LocalServices.user_service as user_service
from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstract_view
import ViewLayer.CLI.menu_view as menu_view
import ViewLayer.CLI.session as session


class NewUserView(abstract_view.AbstractView):
    
    def __init__(self) -> None:
        self.__questions = [{'type': 'input', 'name': 'id_user', 'message': 'Enter an id :'},
                            {'type': 'input', 'name': 'email_user', 'message': 'Enter a Gmail adress :'},
                            {'type': 'password', 'name': 'password_user', 'message': 'Enter a password :'},
                            {'type': 'input', 'name': 'favorite_beer_type', 'message': "Enter your favorite beers' type :"},
                            {'type': 'input', 'name': 'budget_user', 'message': "Enter your budget :", 'filter': float}]

    def make_choice(self):
        answers = prompt(self.__questions)
        succes = user_service.UserService().create_user(answers['id_user'], answers['email_user'], answers['password_user'], 
                                           answers['favorite_beer_type'], answers['budget_user'])
        if not(succes):
            print("Error")
            return NewUserView()
        session.Session().user = session_service.SessionService().open_session(answers['id_user'], answers['password_user'])
        return menu_view.MenuView()