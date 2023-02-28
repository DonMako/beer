import BusinessLayer.LocalServices.session_service as session_service
from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstract_view
import ViewLayer.CLI.find_pubs_view as find_pubs_view
import ViewLayer.CLI.modify_user_view as modify_user_view
import ViewLayer.CLI.session as session
import ViewLayer.CLI.start_view as start_view


class MenuView(abstract_view.AbstractView):
    
    def __init__(self) -> None:
        self.__questions = [{'type': 'list', 'name': 'choice', 'message': 'What do you want to do ?',
                             'choices': ['F) Find bars', 'M) Modify my profile', 'Q) Disconnect']}]

    def make_choice(self):
        if session.Session().user is None:
            return start_view.StartView()
        self.__questions[0]['choices'].append('Q) Me déconnecter')
        answers = prompt(self.__questions)
        if str.upper(answers['choice'][0]) == "F":
            return find_pubs_view.FindPubsView()
        if str.upper(answers['choice'][0]) == "M":
            return modify_user_view.ModifyUserView()
        if str.upper(answers['choice'][0]) == "Q":
            session_service.SessionService().close_session()