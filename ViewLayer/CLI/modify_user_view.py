from BusinessLayer.BusinessObjects.user import User
import BusinessLayer.LocalServices.user_service as user_service
from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstract_view
import ViewLayer.CLI.email_service as email_service
import ViewLayer.CLI.menu_view as menu_view
import ViewLayer.CLI.session as session
import ViewLayer.CLI.start_view as start_view


class ModifyUserView(abstract_view.AbstractView):
    
    def __init__(self, user: User = None) -> None:
        if user is None:
            self.__user = session.Session().user
        else:
            self.__user = user
        self.__main_prompt = [{'type': 'list', 'name': 'choices',
                               'message': 'What do you want to modify ?',
                               'choices': ['P) Password', "F) Favourite beers' type", 'B) Budget', 'D) Delete account']}]
        self.__main_prompt[0]['choices'].append('M) Menu')
        self.__continue_prompt = [{'type': 'list', 'name': 'choices', 'message': 'Modify something else ?', 'choices': ['Y) Yes', 'N) No']}]

    def make_choice(self):
        modify = True
        while modify:
            answers0 = prompt(self.__main_prompt)
            if "M" in str.upper(answers0['choices'][0]):
                modify = False
            else:
                if "P" in str.upper(answers0['choices'][0]):
                    prompt_password = [{'type': 'input', 'name': 'password_user', 'message': "New password :"}]
                    answer = prompt(prompt_password)
                    self.__user.password_user = answer['password']
                    succes = user_service.UserService().modify_user(self.__user)
                    if succes:
                        email_adress = user_service.UserService().modify_user(self.__user)
                        email_service.EMailService.send_email(email_adress, 'password')
                elif "F" in str.upper(answers0['choices'][0]):
                    prompt_favorite_beer_type = [{'type': 'input', 'name': 'favorite_beer_type', 'message': "New favorite beer flavor :"}]
                    answer = prompt(prompt_favorite_beer_type)
                    self.__user.favorite_beer_type = answer['favorite_beer_type']
                    succes = user_service.UserService().modify_user(self.__user)
                    if succes:
                        email_adress = user_service.UserService().modify_user(self.__user)
                        email_service.EMailService.send_email(email_adress, 'favorite beer type')
                elif "B" in str.upper(answers0['choices'][0]):
                    prompt_budget = [{'type': 'input', 'name': 'budget_user', 'message': "New budget :",'filter': float}]
                    answer = prompt(prompt_budget)
                    self.__user.budget_user = answer['budget_user']
                    succes = user_service.UserService().modify_user(self.__user)
                    if succes:
                        email_adress = user_service.UserService().modify_user(self.__user)
                        email_service.EMailService.send_email(email_adress, 'budget')
                elif "D" in str.upper(answers0['choices'][0]):
                    prompt_verif = [{'type': 'input', 'name': 'verif', 'message': "You are about to delete your account. Do you confirm to do this action ?"}]
                    answer = prompt(prompt_verif)
                    if answer:
                        succes = user_service.UserService().delete_user(self.__user)
                        return start_view.StartView()
                else:
                    succes = True
                if not succes:
                    print('Modification failed. Try again later.')
                answer_continue = prompt(self.__continue_prompt)
                modify = str.upper(answer_continue['choices'][0]) == "Y"
        return menu_view.MenuView()