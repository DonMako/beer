from BusinessLayer.BusinessObjects.user import User
import BusinessLayer.LocalServices.pub_service as pub_service
import BusinessLayer.LocalServices.user_service as user_service
from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstract_view
import ViewLayer.CLI.session as session


class FindPubsView(abstract_view.AbstractView):
    
    def __init__(self, user: User = None) -> None:
        if user is None:
            self.__user = session.Session().user
        else:
            self.__user = user
        self.__questions = [{'type': 'input', 'name': 'place', 'message': 'Where are you ?'}]

    def make_choice(self):
        answers = prompt(self.__questions)
        list_pubs_localisation = pub_service.PubService.get_pubs_localisation(answers["place"])
        favorite_beer_type = user_service.UserService.get_favorite_beer_type(self.__user)
        list_pubs_beer_type = pub_service.PubService.get_pubs_beer(list_pubs_localisation, favorite_beer_type)