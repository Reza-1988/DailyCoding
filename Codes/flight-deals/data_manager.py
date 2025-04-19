import requests
from pprint import pprint


from Codes.local_settings import SHEETY_DATA


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self.user = os.environ["SHEET_USERNAME"]
        # self.password = os.environ["SHEET_PASSWORD"]
        # self.auth = (sel.user, sel.password)
        self.destination_data = {}
        self.customers_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        # Go to the link for the starting Google Sheet and make your own sheet.Then create a new project on Sheety to work with your Google sheet.
        # Use the Sheety API to GET all the data in that sheet and print it out. You should see something like this:
        sheety_response = requests.get(SHEETY_DATA["SHEETY_ENDPOINT_PRICES"])
        sheety_response.raise_for_status()
        data = sheety_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_data(self):
        for row in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"],
                }
            }
            response = requests.put(f"{SHEETY_DATA['SHEETY_ENDPOINT_PRICES']}/{row['id']}", json=new_data)

    def get_customer_emails(self):
        response = requests.get(SHEETY_DATA["SHEETY_ENDPOINT_USERS"])
        response.raise_for_status()
        data = response.json()
        self.customers_data = data["users"]
        return self.customers_data


