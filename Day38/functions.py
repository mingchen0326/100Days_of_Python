import requests
from datetime import datetime

## Get food calorie and exercise calorie data from NutritionIX API

def get_food_calorie(message, headers):
    nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    body = {
        "query": message,
        "timezone": "US/Eastern"
    }
    response = requests.request("POST", url=nutritionix_endpoint, json=body, headers=headers)
    return response.text


def get_exercise_calories(message, headers):
    nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    body = {
        "query": message,
        "gender": "male",
        "weight_kg": 72.5,
        "height_cm": 167.64,
        "age": 30
    }
    response = requests.post(url=nutritionix_endpoint, json=body, headers=headers)

    return response.json()



