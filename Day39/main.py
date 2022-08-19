from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.


# Get all designated city names from Google Sheet
data = DataManager()
table = data.get_data()

# convert city names to IATA code
city_dict = {row["city"]: row["id"] for row in table["prices"]}

# create flight database instance
flight_database = FlightSearch()

# Add IATA Code back to Google Sheet
for city in list(city_dict.keys()):
    IATA_code = flight_database.get_IATA(city)
    row_body = {
        "price": {
            "iataCode": IATA_code["locations"][0]["code"],
        }
    }
    put_response = data.update_row(row_body, city_dict[city])

# get IATA code of designation and the target prices from google sheet
IATA_and_Price = {row["iataCode"]: row["lowestPrice"] for row in table["prices"]}
departure_IATA = "LON"

# create SMS notification instance
notification = NotificationManager()

# loop through all designations into database to find available flights
for designation_IATA in list(IATA_and_Price.keys()):
    response_json = flight_database.search_flight(departure_IATA, designation_IATA)
    flight_data = FlightData(response_json)
    target_price = IATA_and_Price[designation_IATA]

    # find the most recent flights below target price
    search_result = flight_data.search_best_flight(target_price)

    # get -1 if no flight is below target price, otherwise, return matching flight information
    if search_result == -1:
        print(f"no matching flights from {departure_IATA} to {designation_IATA}")
    else:
        ticket_price = search_result['ticket_price']
        departure_city = search_result['departure_city']
        departure_airport = search_result['departure_airport']
        arrival_city = search_result['arrival_city']
        arrival_airport = search_result['arrival_airport']
        departure_date = search_result['departure_date']
        return_date = search_result['return_date']
        message = f"Low price alert! Only £{ticket_price} " \
                  f"from {departure_city}-{departure_airport} to {arrival_city}-{arrival_airport}, " \
                  f"from {departure_date} to {return_date}"

        # send the message through SMS
        notification.send_message(message)
