import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
params = {"appid": "Your app id",
          "lat": 40.672291,
          "lon": 122.278069,
          "part": "minutely,daily"}
response = requests.get(url=OWM_Endpoint, params=params)

# api_key = "Your app id"
# lat = 43.159988
# lon = -79.247017
# part = "minutely"
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}")

response.raise_for_status()
weather_data = response.json()
hourly_weather_data = weather_data["hourly"][:12]
weather_id = [hourly_weather["weather"][0]["id"] for hourly_weather in hourly_weather_data]


def will_rain(weather_id):
    for code in weather_id:
        if code < 700:
            return True

    return False


print(will_rain(weather_id))

# for hour in range(12):
#     weather_id = hourly_weather_data[hour]["weather"][0]["id"]
#     print(weather_id)
#     if round(weather_id / 100) < 7:
#         print("bring umbrella")
#     else:
#         print("Do not bring umbrella")

