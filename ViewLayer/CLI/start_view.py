from PyInquirer import prompt
from ViewLayer.CLI.abstract_view import AbstractView
from ViewLayer.CLI.connexion_view import ConnexionView
from ViewLayer.CLI.new_user_view import NewUserView


class StartView(AbstractView):
    def __init__(self):
        self.__questions = [{'type': 'list','name': 'choice','choices': ['C) Connect', 'N) Create account', 'Q) Quit']}]

    def make_choice(self):
        answers = prompt(self.__questions)
        if str.upper(answers['choice'][0]) == "F":
            return ConnexionView()
        elif str.upper(answers['choice'][0]) == "N":
            return NewUserView()
        elif str.upper(answers['choice'][0]) == "Q":
            return None
        else:
            return StartView()