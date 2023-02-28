from BusinessLayer.BusinessObjects.user import User
import BusinessLayer.LocalServices.beer_service as beer_service
import BusinessLayer.LocalServices.menu_service as menu_service
import BusinessLayer.LocalServices.pub_service as pub_service
import BusinessLayer.LocalServices.user_service as user_service
from PyInquirer import prompt
import ViewLayer.CLI.abstract_view as abstract_view
import ViewLayer.CLI.menu_view as menu_view
import ViewLayer.CLI.session as session


class FindPubsView(abstract_view.AbstractView):
    
    def __init__(self, user: User = None) -> None:
        if user is None:
            self.__user = session.Session().user
        else:
            self.__user = user
        self.__questions = [{'type': 'input', 'name': 'place', 'message': 'Where are you ?'}]
        self.__research_prompt = [{'type': 'list', 'name': 'choices', 'message': 'New research ?', 'choices': ['Y) Yes', 'N) No']}]

    def make_choice(self):
        research = True
        while research:
            answers = prompt(self.__questions)
            list_pubs_localised = pub_service.PubService.get_pubs_localisation(answers["place"])
            list_beers_pubs_localised = []
            for pub in list_pubs_localised:
                name_pub = pub_service.PubService.get_name_pub(pub)
                dict = {}
                dict[name_pub] = menu_service.MenuService.get_pub_beers(name_pub)
                list_beers_pubs_localised.append(dict)
            favorite_beer_type = user_service.UserService.get_favorite_beer_type(self.__user)
            list_pubs_localised_type = []
            for dict_pub in list_beers_pubs_localised:
                for beer in list(dict_pub.values()):
                    type_beer = beer_service.BeerService.get_type_beer(beer)
                    if type_beer == favorite_beer_type:
                        list_pubs_localised_type.append(list(dict_pub.key())[0])
            list_pubs_localised_type_budget = []
            for dict_pub in list_beers_pubs_localised:
                for beer in list(dict_pub.values()):
                    type_beer = beer_service.BeerService.get_price_beer(beer)
                    if type_beer == favorite_beer_type:
                        list_pubs_localised_type_budget.append(list(dict_pub.key())[0])
            answer_research = prompt(self.__research_prompt)
            research = str.upper(answer_research['choices'][0]) == "Y"
        return menu_view.MenuView()