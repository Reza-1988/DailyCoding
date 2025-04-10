import requests

GENDER = "male"
WEIGHT_KG = 73
HEIGHT_CM = 173
AGE = 37

APP_ID = "176ec005"
API_KEY = "633308573c7dd5ecec4a7ace0534aec7"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()
print(result)

