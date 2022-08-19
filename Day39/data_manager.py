import os
import requests


class DataManager:

    def __init__(self):
        # API credentials
        self.flight_endpoint = os.environ.get("FLIGHT_ENDPOINT")
        self.user_endpoint = os.environ.get("USER_ENDPOINT")
        self.header = {"Authorization": os.environ.get("SHEETY_TOKEN")}

        # flight tab in google sheet
        self.get_flight_response = ""
        self.post_flight_response = ""
        self.put_flight_response = ""
        self.flight_body = {}

        # user tab in google sheet
        self.get_user_response = ""
        self.post_user_response = ""
        self.put_user_response = ""
        self.user_body = {}

    def get_flight(self):
        self.get_flight_response = requests.get(url=self.flight_endpoint, headers=self.header)
        return self.get_flight_response.json()

    def post_flight(self, flight_body):
        self.post_flight_response = requests.post(url=self.flight_endpoint, json=flight_body, headers=self.header)
        return self.post_flight_response.text

    def update_flight(self, data, row_id):
        self.put_flight_response = requests.put(url=self.flight_endpoint + f"/{row_id}", json=data, headers=self.header)
        return self.put_flight_response.text

    def get_user(self):
        self.get_flight_response = requests.get(url=self.user_endpoint, headers=self.header)
        return self.get_flight_response.json()

    def post_user(self, user_body):
        self.post_flight_response = requests.post(url=self.user_endpoint, json=user_body, headers=self.header)
        return self.post_flight_response.text

    def update_user(self, data, row_id):
        self.put_flight_response = requests.put(url=self.user_endpoint + f"/{row_id}", json=data, headers=self.header)
        return self.put_flight_response.text


