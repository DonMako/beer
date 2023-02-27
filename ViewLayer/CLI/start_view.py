from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstractView
import ViewLayer.CLI.connexion_view as connexionView
import ViewLayer.CLI.new_user_view as newUserView


class StartView(abstractView.AbstractView):
    def __init__(self):
        self.__questions = [{'type': 'list','name': 'choices', 'message': 'What do you want to do ?', 
                             'choices': ['C) Connect', 'N) Create account', 'Q) Quit']}]

    def make_choice(self):
        answers = prompt(self.__questions)
        if str.upper(answers['choices'][0]) == "C":
            return connexionView.ConnexionView()
        elif str.upper(answers['choices'][0]) == "N":
            return newUserView.NewUserView()
        elif str.upper(answers['choices'][0]) == "Q":
            return None
        else:
            return StartView()