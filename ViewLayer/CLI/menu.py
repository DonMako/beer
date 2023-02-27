import BusinessLayer.LocalServices.session_service as sessionService
from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstractView
import ViewLayer.CLI.find_pubs_view as findPubsView
import ViewLayer.CLI.modify_user_view as modifyUserView
import ViewLayer.CLI.session as session
import ViewLayer.CLI.start_view as startView


class MenuView(abstractView.AbstractView):
    
    def __init__(self) -> None:
        self.__questions = [{'type': 'list', 'name': 'choice', 'message': 'What do you want to do ?',
                             'choices': ['F) Find bars', 'M) Modify my profile', 'Q) Disconnect']}]

    def make_choice(self):
        if session.Session().user is None:
            return startView.StartView()
        self.__questions[0]['choices'].append('Q) Me déconnecter')
        answers = prompt(self.__questions)
        if str.upper(answers['choice'][0]) == "F":
            return findPubsView.FindPubsView()
        if str.upper(answers['choice'][0]) == "M":
            return modifyUserView.ModifyUserView()
        if str.upper(answers['choice'][0]) == "Q":
            sessionService.SessionService().close_session()