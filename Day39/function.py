# get -1 if no flight is below target price, otherwise, return matching flight information
def compose_msg(search_result, departure_IATA, designation_IATA):
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
    return message

def get_user_info():
    print("Welcome to Ming's Flight Club\n"
          "We find the best flight deal and email to you.")
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    email = input("What is your email?")
    retype_email = input("Type your email again.")
    if email == retype_email:
        return {
            "user": {"firstName": first_name,
                   "lastName": last_name,
                   "email": email}
        }
    else:
        return -1

def add_IATA_to_sheet(city_dict, flight_database, sheet_instance):
    for city in list(city_dict.keys()):
        IATA_code = flight_database.get_IATA(city)
        row_body = {
            "price": {
                "iataCode": IATA_code["locations"][0]["code"],
            }
        }
        put_response = sheet_instance.update_flight(row_body, city_dict[city])