import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


# Set your origin airport
ORIGIN_CITY_IATA = "LON"

flight_search = FlightSearch()

# Make an object from DataManager class and get all data in google sheet in sheet data variable.
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

# Looking for IATA code in sheet data if is not exist getting from flight search.
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
print(f"sheet data:\n {sheet_data}")
data_manager.destination_data = sheet_data
data_manager.update_destination_data()

# Get customer email from users a Google sheet.
customer_data = data_manager.get_customer_emails()
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]

# Set beginning and ending time for ticket search.
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.today() + timedelta(days=180)

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today,
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    time.sleep(2)

    # If there isn't any direct flight to our destination, change the is_direct parameter to False.
    if cheapest_flight.price != "N/A":
        print(
            f"No direct flight to {destination['city']}. looking for indirect flights..."
        )
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_months_from_today,
            is_direct=False,
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"cheapest indirect flight price is: £{cheapest_flight.price}")

    # If any least expensive flight found sending email for customers and sms for ourselves.
    if (
        cheapest_flight.price != "N/A"
        and cheapest_flight.price < destination["lowestPrice"]
    ):
        # Customise the message depending on the number of stops
        if cheapest_flight.stops == 0:
            message = (
                f"Low price alert! Only GBP {cheapest_flight.price} to fly direct "
                f"from {cheapest_flight.origin} to {cheapest_flight.destination}, "
                f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )
        else:
            message = (
                f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                f"from {cheapest_flight.origin} to {cheapest_flight.destination}, "
                f"with {cheapest_flight.stops} stop(s) "
                f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."
            )
        print(f"Check your email. Lower price flight found to {destination['city']}!")

        # notification_manager.send_sms(message_body=message)
        notification_manager = NotificationManager()
        notification_manager.send_sms(body_message=message)

        # Send emails to everyone on the list
        notification_manager.send_email(
            email_list=customer_email_list, email_body=message
        )
