import os
import requests
from twilio.rest import Client

# Twilio account info
account_sid = "Your accoun_sid from dashboard"
auth_token = "Your auth_token from dashboard"
twilio_phone_number = "Your twilio phone number"

# OWM API info
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
params = {"appid": "Your app id",
          "lat": 40.672291,
          "lon": 122.278069,
          "part": "minutely,daily"}
response = requests.get(url=OWM_Endpoint, params=params)

# raise error if response is not 200
response.raise_for_status()

# extract weather id from json data
weather_data = response.json()
hourly_weather_data = weather_data["hourly"][:12]
weather_id = [hourly_weather["weather"][0]["id"] for hourly_weather in hourly_weather_data]

# whether it will rain in the next 12 hours based on weather id
def will_rain(weather_id):
    for code in weather_id:
        if code < 700:
            return True

    return False

# send message if it will rain
if will_rain(weather_id):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain in the next 12 hours, bring the umbrella!",
        from_=twilio_phone_number,
        to='the phone number you want to send message to'
    )
    print(message.status)


# Download the helper library from https://www.twilio.com/docs/python/install
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure




