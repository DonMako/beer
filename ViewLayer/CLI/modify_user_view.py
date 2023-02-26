from PyInquirer import prompt
from BusinessLayer.LocalServices.user_service import UserService
from ViewLayer.CLI.abstract_view import AbstractView
from ViewLayer.CLI.session import Session
from BusinessLayer.BusinessObjects.user import User
import ViewLayer.CLI.menu as menu


class ModifierUserView(AbstractView):
    def __init__(self, user: User = None) -> None:
        if user is None:
            self.__user = Session().user
        else:
            self.__user = user
        self.__main_prompt = [{'type': 'list', 'name': 'choice',
                               'message': 'What do you want to modify ?',
                               'choices': ['I) Id', 'P) Password', "F) Favourite beer's flavour", 'B) Budget']}]
        self.__main_prompt[0]['choices'].append('M) Menu')
        self.__continue_prompt = [{'type': 'list', 'name': 'choice', 'message': 'Modify something else ?',
                                   'choices': ['Y) Yes', 'N) No']}]

    def make_choice(self):
        modify = True
        while modify:
            answers0 = prompt(self.__main_prompt)
            if str.upper(answers0['choices'][0]) == "M":
                modify = False
            else:
                if str.upper(answers0['choices'][0]) == "I":
                    prompt_id = [{'type': 'input', 'name': 'id', 'message': "New id :"}]
                    answer = prompt(prompt_id)
                    self.__user.id = answer['id']
                    succes = UserService().modify_user(self.__user)
                elif str.upper(answers0['choices'][0]) == "P":
                    prompt_password = [{'type': 'input', 'name': 'password', 'message': "New password :"}]
                    answer = prompt(prompt_password)
                    self.__user.password = answer['password']
                    succes = UserService().modify_user(self.__user)
                elif str.upper(answers0['choices'][0]) == "F":
                    prompt_favorite_beer_flavor = [{'type': 'input', 'name': 'favorite_beer_flavor', 'message': "New favorite beer flavor :"}]
                    answer = prompt(prompt_favorite_beer_flavor)
                    self.__user.favorite_beer_flavor = answer['favorite_beer_flavor']
                    succes = UserService().modify_user(self.__user)
                elif str.upper(answers0['choices'][0]) == "B":
                    prompt_budget = [{'type': 'input', 'name': 'budget', 'message': "New budget :",'filter': float}]
                    answer = prompt(prompt_budget)
                    self.__user.budget = answer['budget']
                    succes = UserService().modify_user(self.__user)
                else:
                    succes = True
                if not succes:
                    print('Modification failed. Try again later.')
                answer_continue = prompt(self.__continue_prompt)
                modify = str.upper(answer_continue['choice'][0]) == "Y"
        return menu.MenuPrincipalView()