import requests
import os
from datetime import datetime

## Step 1: create username
pixela_endpoint = os.environ.get("PIXELA_ENDPOINT")
TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

## Step 2: create a graph definition
ID = os.environ.get("GRAPH_ID")
ID_list = []

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


## Step 4: Add value to the graph
today = datetime.now()
print(today)
post_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
post_value_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50"
}

# response3 = requests.post(url=post_value_endpoint, json=post_value_params, headers=headers)
# print(response3.text)

# to update the graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {"quantity": "4.5"}

requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
