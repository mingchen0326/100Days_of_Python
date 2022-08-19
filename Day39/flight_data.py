class FlightData:

    def __init__(self, flight_result):
        self.search_result = flight_result["data"]
        self.search_result.reverse()
        self.departure_date = ""
        self.return_date = ""
        self.message = ""

    def search_best_flight(self, target_price):
        for flight in self.search_result:
            if flight["price"] < target_price:
                travel_info = {
                    "ticket_price": flight["price"],
                    "departure_airport": flight["flyFrom"],
                    "arrival_airport": flight["flyTo"],
                    "departure_city": flight["cityFrom"],
                    "arrival_city": flight["cityTo"],
                    "departure_date": flight["route"][0]["local_departure"].split("T")[0],
                    "return_date": flight["route"][1]["local_departure"].split("T")[0]
                    }
                return travel_info

        return -1

