import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


# Set your origin airport
ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

for row in sheet_data:
    if row["iataCode"] == "":
        row['iataCode'] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
print(f"sheet data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_data()


tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.today() + timedelta(days=180)

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    time.sleep(2)

    if cheapest_flight.price != "N/A":
        print(f"No direct flight to {destination['city']}. looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_months_from_today,
            is_direct = False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"cheapest indirect flight price is: £{cheapest_flight.price}")

        notification_manager = NotificationManager()
        notification_manager.send(f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin} to {cheapest_flight.destination}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
    # Slowing down requests to avoid rate limit
    time.sleep(2)
