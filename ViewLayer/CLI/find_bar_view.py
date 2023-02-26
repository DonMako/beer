from PyInquirer import prompt
from ViewLayer.CLI.abstract_view import AbstractView
from ViewLayer.CLI.modify_user_view import ModifyUserView


class FindBarView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [{'type': 'input', 'name': 'place', 'message': 'Where are you ?'}]

    def make_choice(self):
        answers = prompt(self.__questions)