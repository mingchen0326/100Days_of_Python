import os
import requests


class DataManager:

    def __init__(self):
        self.sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
        self.get_response = ""
        self.post_response = ""
        self.body = {}
        self.header = {"Authorization": os.environ.get("SHEETY_TOKEN")}

    def get_data(self):
        self.get_response = requests.get(url=self.sheety_endpoint)
        return self.get_response.text

    def post_data(self, body):
        # self.body = {
        #     "price": {
        #         "city": "Tokyo",
        #         "iataCode": "",
        #         "lowestPrice": 50,
        #         "id": 11
        #     }
        # }
        self.post_response = requests.post(url=self.sheety_endpoint, json=body, headers=self.header)
        return self.post_response.text
