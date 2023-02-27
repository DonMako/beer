from BusinessLayer.BusinessObjects.user import User
from BusinessLayer.LocalServices.user_service import UserService
from PyInquirer import prompt
from ViewLayer.CLI.abstract_view import AbstractView
from ViewLayer.CLI.menu import MenuView
from ViewLayer.CLI.session import Session
from ViewLayer.CLI.start_view import StartView


class ModifyUserView(AbstractView):
    def __init__(self, user: User = None) -> None:
        if user is None:
            self.__user = Session().user
        else:
            self.__user = user
        self.__main_prompt = [{'type': 'list', 'name': 'choices',
                               'message': 'What do you want to modify ?',
                               'choices': ['M) Mailing adress', 'P) Password', "F) Favourite beer's flavour", 'B) Budget', 'D) Delete account']}]
        self.__main_prompt[0]['choices'].append('H) Menu')
        self.__continue_prompt = [{'type': 'list', 'name': 'choices', 'message': 'Modify something else ?',
                                   'choices': ['Y) Yes', 'N) No']}]

    def make_choice(self):
        modify = True
        while modify:
            answers0 = prompt(self.__main_prompt)
            if "H" in str.upper(answers0['choices'][0]):
                modify = False
            else:
                if "M" in str.upper(answers0['choices'][0]):
                    prompt_mail = [{'type': 'input', 'name': 'mail_user', 'message': "New mailing adress :"}]
                    answer = prompt(prompt_mail)
                    self.__user.mail_user = answer['mail_user']
                    succes = UserService().modify_user(self.__user)
                elif "P" in str.upper(answers0['choices'][0]):
                    prompt_password = [{'type': 'input', 'name': 'password_user', 'message': "New password :"}]
                    answer = prompt(prompt_password)
                    self.__user.password_user = answer['password']
                    succes = UserService().modify_user(self.__user)
                elif "F" in str.upper(answers0['choices'][0]):
                    prompt_favorite_beer_flavor = [{'type': 'input', 'name': 'favorite_beer_flavor', 'message': "New favorite beer flavor :"}]
                    answer = prompt(prompt_favorite_beer_flavor)
                    self.__user.favorite_beer_flavor = answer['favorite_beer_flavor']
                    succes = UserService().modify_user(self.__user)
                elif "B" in str.upper(answers0['choices'][0]):
                    prompt_budget = [{'type': 'input', 'name': 'budget_user', 'message': "New budget :",'filter': float}]
                    answer = prompt(prompt_budget)
                    self.__user.budget_user = answer['budget_user']
                    succes = UserService().modify_user(self.__user)
                elif "D" in str.upper(answers0['choices'][0]):
                    prompt_verif = [{'type': 'input', 'name': 'verif', 'message': "You are about to delete your account. Do you confirm to do this action ?"}]
                    answer = prompt(prompt_verif)
                    if answer:
                        succes = UserService().delete_user(self.__user)
                        return StartView()
                else:
                    succes = True
                if not succes:
                    print('Modification failed. Try again later.')
                answer_continue = prompt(self.__continue_prompt)
                modify = str.upper(answer_continue['choice'][0]) == "Y"
        return MenuView()