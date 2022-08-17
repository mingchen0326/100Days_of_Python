import os
import requests
from datetime import datetime
from datetime import timedelta


class FlightSearch:

    def __init__(self):
        # location API and endpoint
        self.location_apikey = os.environ.get("TEQUILA_LOCATION_APIKEY")
        self.location_header = {"apikey": self.location_apikey}
        self.location_endpoint = os.environ.get("TEQUILA_LOCATION_ENDPOINT")
        print(self.location_apikey)
        print(self.location_endpoint)
        self.location_params = {}
        self.location_response = ""
        # Search flight API and endpoints
        self.search_apikey = os.environ.get("TEQUILA_SEARCH_APIKEY")
        self.search_header = {"apikey": self.search_apikey}
        self.search_endpoint = os.environ.get("TEQUILA_SEARCH_ENDPOINT")
        self.search_params = {}
        self.search_response = ""

        self.date_from = datetime.now().date()
        self.date_to = (self.date_from + timedelta(days=180))
        self.format_date_from = self.date_from.strftime("%d/%m/%Y")
        self.format_date_to = self.date_to.strftime("%d/%m/%Y")

    def get_IATA(self):
        self.location_params = {
            "term": "London",
            "locale": "en-US"
        }
        self.location_response = requests.get(url=self.location_endpoint, params=self.location_params, headers=self.location_header)
        return self.location_response.json()

    def search_flight(self):
        self.search_params = {
            "fly_from": "LON",
            "fly_to": "PAR",
            "date_from": self.format_date_from,
            "date_to": self.format_date_to
        }
        self.search_response = requests.get(url=self.search_endpoint, params=self.search_params, headers=self.search_header)
        return self.search_response.json()
