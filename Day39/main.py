from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from function import *

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.


# Get all designated city names from Google Sheet
data = DataManager()
flight_table = data.get_flight()
user_table = data.get_user()
print(user_table)
user_info = get_user_info()
data.post_user(user_info)

# convert city names to IATA code
city_dict = {row["city"]: row["id"] for row in flight_table["prices"]}

# create flight database instance
flight_database = FlightSearch()

# Add IATA Code back to Google Sheet
add_IATA_to_sheet(city_dict, flight_database, data)

# get IATA code of designation and the target prices from google sheet
IATA_and_Price = {row["iataCode"]: row["lowestPrice"] for row in flight_table["prices"]}
departure_IATA = "LON"

# create SMS notification instance
notification = NotificationManager()

# loop through all designations into database to find available flights
for designation_IATA in list(IATA_and_Price.keys()):
    direct = False
    stopover = False
    response_direct = flight_database.search_direct_flight(departure_IATA, designation_IATA)
    target_price = IATA_and_Price[designation_IATA]
    # find the most recent direct flights below target price
    search_direct = FlightData(response_direct).search_best_flight(target_price)

    # get -1 if no flight is below target price, otherwise, return matching flight information
    if search_direct == -1:
        print(f"no direct flights from {departure_IATA} to {designation_IATA}")
        response_stopover = flight_database.search_stopover_flight(departure_IATA, designation_IATA)
        # find the most recent 1 stopover flights below target price
        search_stopover = FlightData(response_direct).search_best_flight(target_price)
        if search_stopover != -1:
            stopover = True
    else:
        direct = True

    if direct:
        message = compose_msg(search_direct, departure_IATA, designation_IATA)
        notification.send_message(message)
    elif stopover:
        message = compose_msg(search_stopover, departure_IATA, designation_IATA)
        notification.send_message(message)


