import os
import requests

AMADEUS_API_KEY = os.environ.get('AMADEUS_API_KEY', "TXmatvZo4bNuqADAoxAIMNV409CTsO2l")
AMADEUS_API_SECRET = os.environ.get('AMADEUS_API_SECRET', "534KKs3f0350Bctt")
TOKEN_ENDPOINT = os.environ.get('TOKEN_ENDPOINT', "https://test.api.amadeus.com/v1/security/oauth2/token")



class FlightSearch:
    """
           Initialize an instance of the FlightSearch class.
           This constructor performs the following tasks:
           1. Retrieve the API key and secret from the environment variables 'AMADEUS_API_KEY'
           and 'AMADEUS_SECRET' respectively.
           Instance Variables:
           _api_key (str): The API key for authenticating with Amadeus, sourced from the .env file
           _api_secret (str): The API secret for authenticating with Amadeus, sourced from the .env file.
           _token (str): The authentication token obtained by calling the _get_new_token() method.
           """
    def __init__(self):
        self.api_key = AMADEUS_API_KEY
        self.api_secret = AMADEUS_API_SECRET
        # Getting a new token every time program is run. Could reuse unexpired tokens as an extension.
        self._token = self._get_new_token()


    def _get_new_token(self):
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret,
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(response.text)


    def get_destination_code(self, city_name):
        code = "Testing"
        return code


flight_search = FlightSearch()
flight_search._get_new_token()