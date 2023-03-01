from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstract_view
import ViewLayer.CLI.connexion_view as connexion_view
import ViewLayer.CLI.new_user_view as new_user_view


class StartView(abstract_view.AbstractView):
    
    def __init__(self):
        self.__questions = [{'type': 'list','name': 'choice', 'message': 'What do you want to do ?', 
                             'choices': ['C) Connect', 'N) Create account', 'Q) Quit']}]

    def make_choice(self):
        answers = prompt(self.__questions)
        if answers['choice'][0] == 'C':
            return connexion_view.ConnexionView()
        elif answers['choice'][0] == "N":
            return new_user_view.NewUserView()
        elif answers['choice'][0] == "Q":
            return None
        else:
            return StartView()