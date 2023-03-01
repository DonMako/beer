import urllib.request
import json


def get_itinerary(starting_adress: str, final_adress: str): 
    with open('./utils/api_key.txt') as f:
        api_key = f.readline()
        f.close
    encodedDest = urllib.parse.quote(destination_adress, safe='')
    routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Walking?wp.0=" + starting_adress + "&wp.1=" + final_adress + "&optmz=distance&key=" + api_key
    request = urllib.request.Request(routeUrl)
    response = urllib.request.urlopen(request)
    r = response.read().decode(encoding="utf-8")
    result = json.loads(r)
    itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]
    for item in itineraryItems:
        print(item["instruction"]["text"])

# L'utilisateur indique l'adresse qu'il choisit et le lieu où il se trouve, et récupère le trajet qu'il doit suivre.
# Possibilité d'avoir des noms de bière en favori