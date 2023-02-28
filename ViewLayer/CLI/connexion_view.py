from BusinessLayer.BusinessObjects.user import User
import BusinessLayer.LocalServices.session_service as session_service
from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstract_view
import ViewLayer.CLI.menu as menu_view
import ViewLayer.CLI.session as session


class ConnexionView(abstract_view.AbstractView):
    
    def __init__(self) -> None:
        self.__questions = [{'type': 'input', 'name': 'id_user', 'message': 'Username :'},
                            {'type': 'password', 'name': 'password_user', 'message': 'Password :'}]
        self.__error = "Incorrect username and/or password."

    def make_choice(self):
        answers = prompt(self.__questions)
        user = session_service.SessionService().open_session(answers['id_user'], answers['password_user'])
        if not (isinstance(user, User)):
            print(self.__error)
            return ConnexionView()
        session.Session().user = user
        return menu_view.MenuView()