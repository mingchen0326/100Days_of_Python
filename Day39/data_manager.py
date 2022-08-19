import os
import requests


class DataManager:

    def __init__(self):
        self.sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
        self.get_response = ""
        self.post_response = ""
        self.put_response = ""
        self.body = {}
        self.header = {"Authorization": os.environ.get("SHEETY_TOKEN")}

    def get_data(self):
        self.get_response = requests.get(url=self.sheety_endpoint, headers=self.header)
        return self.get_response.json()

    def post_data(self, body):
        self.post_response = requests.post(url=self.sheety_endpoint, json=body, headers=self.header)
        return self.post_response.text

    def update_row(self, data, row_id):
        self.put_response = requests.put(url=self.sheety_endpoint + f"/{row_id}", json=data, headers=self.header)
        return self.put_response.text
