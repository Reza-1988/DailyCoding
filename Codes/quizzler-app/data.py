import requests

# To change the question category, update the value of category key
parameters = {
    'amount': 10,
    'type': 'boolean',
    'category': 18
}
# get API from this website -> https://opentdb.com/
response = requests.get("https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data["results"]



