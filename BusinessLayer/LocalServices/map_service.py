import json
import urllib.request


def get_itinerary(starting_adress: str, final_adress: str): 
    with open('./utils/api_key.txt') as f:
        api_key = f.readline()
        f.close
    routeUrl = "http://dev.virtualearth.net/REST/V1/Routes/Walking?wp.0=" + starting_adress + "&wp.1=" + final_adress + "&optmz=distance&key=" + api_key
    request = urllib.request.Request(routeUrl)
    response = urllib.request.urlopen(request)
    r = response.read().decode(encoding="utf-8")
    result = json.loads(r)
    informationItems = result["resourceSets"][0]["resources"][0]
    itineraryItems = informationItems["routeLegs"][0]["itineraryItems"]
    print("Travel distance:" + informationItems["travelDistance"]+ "km\nTravel duration:" + informationItems["travelDuration"] // 60 + "min")
    for item in itineraryItems:
        print(item["instruction"]["text"])