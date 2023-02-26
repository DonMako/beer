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
            self.__modal = False
        else:
            self.__user = user
            self.__modal = True
        self.__main_prompt = [{'type': 'list', 'name': 'choices',
                               'message': 'What do you want to modify ?',
                               'choices': ['I) Id', 'P) Password', "F) Favourite beer's flavour"]}]
        self.__main_prompt[0]['choices'].append('M) Menu')
        self.__continue_prompt = [{'type': 'list', 'name': 'choices', 'message': 'Modify something else ?',
                                   'choices': ['Y) Yes', 'N) No']}]

    #def display_info(self):
    #    print('   Agent n°:' + str(self.__agent.agent_id) + '\nPrénom : ' + str(self.__agent.prenom) +
    #          '\nNom : ' + str(self.__agent.nom) + '\nQuotité de travail : ' + str(self.__agent.quotite))

    def make_choice(self):
        modify = True
        while modify:
            answers0 = prompt(self.__main_prompt)
            if str.upper(answers0['choices'][0]) == "M":
                modify = False
            else:
                if str.upper(answers0['choices'][0]) == "S":
                    prompt_surname = [{'type': 'input', 'name': 'surname', 'message': "New surname :"}]
                    answer = prompt(prompt_surname)
                    self.__user.surname = answer['surname']
                    succes = UserService().modify_user(self.__user)
                elif str.upper(answers0['choices'][0]) == "N":
                    prompt_nom = [{'type': 'input', 'name': 'name', 'message': "New name :"}]
                    answer = prompt(prompt_nom)
                    self.__agent.nom = answer['name']
                    succes = UserService().modify_user(self.__agent)
                elif str.upper(answers0['choices'][0]) == "T":
                    prompt_quotite = [{'type': 'input', 'name': 'quotite',
                                       'message': "Quelle est la nouvelle quotité de travail ?"}]
                    answers = prompt(prompt_quotite)
                    self.__agent.quotite = answers['quotite']
                    succes = UserService().modify_user(self.__agent)
                elif str.upper(answers0['choices'][0]) == "I":
                    prompt_chgmt = [{'type': 'input', 'name': 'login', 'message': "Quel est votre nom d'utilisateur ?"},
                                    {'type': 'password', 'name': 'mdp', 'message': "Quel est votre mot de passe ?"},
                                    {'type': 'input', 'name': 'n_login',
                                     'message': "Quel est votre nouveau nom d'utilisateur "
                                                "(laisser vide pour ne pas modifier) ?"},
                                    {'type': 'password', 'name': 'n_mdp',
                                     'message': "Quel est votre nouveau mot de passe "
                                                "(laisser vide pour ne pas modifier) ?"}]
                    answer = prompt(prompt_chgmt)
                    if answer['n_login'] == '':
                        answer['n_login'] = None
                    if answer['n_mdp'] == '':
                        answer['n_mdp'] = None
                    succes = UserService().changer_identifiants(self.__agent.agent_id, answer['login'], answer['mdp'],
                                                                 answer['n_login'], answer['n_mdp'])
                elif str.upper(answers0['choices'][0]) == "R":
                    prompt_reinit = [{'type': 'input', 'name': 'n_login',
                                      'message': "Quel est le nouveau nom d'utilisateur "
                                                 "(laisser vide pour ne pas modifier) ?"},
                                     {'type': 'password', 'name': 'n_mdp',
                                      'message': "Quel est le nouveau mot de passe (obligatoire) ?"}]
                    answer = prompt(prompt_reinit)
                    if answer['n_login'] == '':
                        answer['n_login'] = None
                    succes = UserService().reinitialiser_identifiants(self.__agent.agent_id, answer['n_mdp'],
                                                                       answer['n_login'])
                else:
                    succes = True
                if not succes:
                    print('Modification failed. Try again later.')
                answer_continue = prompt(self.__continue_prompt)
                modify = str.upper(answer_continue['choice'][0]) == "Y"
        return menu.MenuPrincipalView()