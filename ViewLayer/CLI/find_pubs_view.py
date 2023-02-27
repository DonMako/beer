from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstractView


class FindPubsView(abstractView.AbstractView):
    def __init__(self) -> None:
        self.__questions = [{'type': 'input', 'name': 'place', 'message': 'Where are you ?'}]

    def make_choice(self):
        answers = prompt(self.__questions)