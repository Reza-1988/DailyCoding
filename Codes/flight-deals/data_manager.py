import requests


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
        return self.destination_data

    def update_destination_data(self):
        for row in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"],
                }
            }
            response = requests.put(f"{SHEETY_ENDPOINT}/{row['id']}", json=new_data)


destination_data =[{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
                   {'city': 'Frankfurt', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
                   {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
                   {'city': 'Hong Kong', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
                   {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
                   {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
                   {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
                   {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
                   {'city': 'Dublin', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]