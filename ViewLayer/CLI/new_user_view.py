import BusinessLayer.LocalServices.email_service as email_service
import BusinessLayer.LocalServices.session_service as session_service
import BusinessLayer.LocalServices.user_service as user_service
import BusinessLayer.LocalServices.email_service as email_service
from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstract_view
import ViewLayer.CLI.start_view as start_view


class NewUserView(abstract_view.AbstractView):
    
    def __init__(self) -> None:
        self.__questions = [{'type': 'input', 'name': 'id_user', 'message': 'Enter an id :'},
                            {'type': 'input', 'name': 'email_user', 'message': 'Enter a Gmail adress :'},
                            {'type': 'password', 'name': 'password_user', 'message': 'Enter a password :'},
                            {'type': 'input', 'name': 'favorite_beer_type', 'message': "Enter your favorite beers' type :"},
                            {'type': 'input', 'name': 'favorite_beer_name', 'message': "Enter your favorite beers' name(s) :"},
                            {'type': 'input', 'name': 'budget_user', 'message': "Enter your budget :", 'filter': float}]
        self.__question_email = [{'type': 'input', 'name': 'email_user', 'message': 'Enter a Gmail adress :'}]

    def make_choice(self):
        answers = prompt(self.__questions)
        while not(email_service.EMailService.check_valid_email(answers["email_user"])):
            print("Invalid Gmail adress.")
            answer_email = prompt(self.__question_email)
            answers["email_user"] = answer_email["email_user"]
        succes = user_service.UserService().create_user(answers['id_user'], answers['email_user'], answers['password_user'], 
                                           answers['favorite_beer_type'], answers['favorite_beer_name'], answers['budget_user'])
        if not(succes):
            print("Error")
            return NewUserView()
        return start_view.StartView()