import os
import requests
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


#------------------------------------------------ Access Sheety Google Sheet -----------------------------------------



#------------------------------------------------ Tequila Search -----------------------------------------
search = FlightSearch()
location = search.get_IATA()
print(location["locations"][0]["code"])
# response_text = search.search_flight()
# price = response_text["data"][0]["price"]
# print(f"the price is {price}")


