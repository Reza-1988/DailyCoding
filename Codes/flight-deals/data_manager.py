import os
import requests
from pprint import pprint


SHEETY_ENDPOINT = "https://api.sheety.co/46f6fe843e43c835235844778aa64ce1/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self.user = os.environ["SHEET_USERNAME"]
        # self.password = os.environ["SHEET_PASSWORD"]
        # self.auth = (sel.user, sel.password)
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        # Go to the link for the starting Google Sheet and make your own sheet.Then create a new project on Sheety to work with your Google sheet.
        # Use the Sheety API to GET all the data in that sheet and print it out. You should see something like this:
        sheety_response = requests.get(SHEETY_ENDPOINT)
        sheety_response.raise_for_status()
        data = sheety_response.json()
        self.destination_data = data["prices"]
        pprint(self.destination_data)  # printing the data out again using pprint() to see it formatted.
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

