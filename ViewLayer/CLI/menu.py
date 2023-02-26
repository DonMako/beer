from PyInquirer import prompt
from BusinessLayer.LocalServices.session_service import SessionService
from ViewLayer.CLI.abstract_view import AbstractView
from ViewLayer.CLI.find_bar_view import FindBarView
from ViewLayer.CLI.modify_user_view import ModifyUserView
import ViewLayer.CLI.start_view as start
from ViewLayer.CLI.session import Session


class MenuView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [{'type': 'list', 'name': 'choice', 'message': 'What do you want to do ?',
                             'choices': ['F) Find bars', 'M) Modify my profile', 'Q) Disconnect']}]

    def make_choice(self):
        if Session().user is None:
            return start.StartView()
        self.__questions[0]['choices'].append('Q) Me déconnecter')
        answers = prompt(self.__questions)
        if str.upper(answers['choice'][0]) == "F":
            return FindBarView()
        if str.upper(answers['choice'][0]) == "M":
            return ModifyUserView()
        if str.upper(answers['choice'][0]) == "Q":
            SessionService().close_session()