import requests

parameters = {
    'amount': 10,
    'type': 'boolean'
}
# get API from this website -> https://opentdb.com/
response = requests.get("https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data["results"]



