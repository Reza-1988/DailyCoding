from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for dict in sheet_data:
        dict['iataCode'] = flight_search.get_destination_code(dict['city'])
    pprint(sheet_data)



data_manager.destination_data = sheet_data
data_manager.update_destination_data()