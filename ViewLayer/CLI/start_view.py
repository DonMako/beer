from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstractView
import ViewLayer.CLI.connexion_view as connexionView
import ViewLayer.CLI.new_user_view as newUserView


class StartView(abstractView.AbstractView):
    def __init__(self):
        self.__questions = [{'type': 'list','name': 'choice','choices': ['C) Connect', 'N) Create account', 'Q) Quit']}]

    def make_choice(self):
        answers = prompt(self.__questions)
        if str.upper(answers['choice'][0]) == "C":
            return connexionView.ConnexionView()
        elif str.upper(answers['choice'][0]) == "N":
            return newUserView.NewUserView()
        elif str.upper(answers['choice'][0]) == "Q":
            return None
        else:
            return StartView()