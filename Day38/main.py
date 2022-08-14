import requests
import os
import json
from functions import *

app_id = os.environ.get("NUTRITIONIX_APP_ID")
app_key = os.environ.get("NUTRITIONIX_APP_KEY")

headers = {"Content - Type": "application / json",
           "x-app-id": app_id,
           "x-app-key": app_key,
           "x-remote-user-id": "0"}


msg__exercise_input = input("Please enter exercise the message: ")
response = get_exercise_calories(msg__exercise_input, headers)


############################### Get google sheet from API ###############################
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
token = os.environ.get("SHEETY_TOKEN")
header = {"Authorization": token}
response_sheet = requests.get(url=sheety_endpoint, headers=header)

# add row to google sheet from API
date = datetime.now().date().strftime("%d/%m/%Y")
time = datetime.now().time().strftime("%X")

for row in response["exercises"]:
    data = {
        "workouts": {
            "date": date,
            "time": time,
            "exercise": row["name"].title(),
            "duration": row["duration_min"],
            "calories": row["nf_calories"],
        }
    }
    add_row_response = requests.post(url=sheety_endpoint, json=data, headers=header)