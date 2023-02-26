from PyInquirer import prompt
from ViewLayer.CLI.abstract_view import AbstractView


class FindPubsView(AbstractView):
    def __init__(self) -> None:
        self.__questions = [{'type': 'input', 'name': 'place', 'message': 'Where are you ?'}]

    def make_choice(self):
        answers = prompt(self.__questions)