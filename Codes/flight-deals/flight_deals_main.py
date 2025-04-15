import time
from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

print(sheet_data)
for row in sheet_data:
    row['iataCode'] = flight_search.get_destination_code(row["city"])
    time.sleep(2)
print(f"sheet data:\n {sheet_data}")

data_manager.update_destination_data()