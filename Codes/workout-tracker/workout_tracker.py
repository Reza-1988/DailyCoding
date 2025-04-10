from datetime import datetime
import requests


GENDER = "male"
WEIGHT_KG = 73
HEIGHT_CM = 173
AGE = 37


# STEP 1- Setup Nutritionix API
# Go to the Nutritionix API website and select "Get Your API Key" to sign up for a free account.
# Double-check your spam folder (and/or your gmail "promotions" tab) for the Nutritionix verification email.
# Once logged in, you should be able to access your API key and App id:
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
results = response.json()


# STEP 2- SETUP SHEETY API
# 1- Log into Sheety with your Google Account (the same account that owns the Google Sheet you copied in step 1).
# 2- Make sure you give Sheety permission to access your Google sheets. If you miss this step, log out of Sheety and log in again.
# 3- Make sure the email matches between your Google Sheet and Sheety Account. e.g.
# 4-  In your project page, click on "New Project" and create a new project in Sheety with the name "Workout Tracking" and paste in the URL of your own "My Workouts" Google Sheet.
# 5- Click on the workouts API endpoint and enable GET and POST.


sheet_endpoint = "https://api.sheety.co/46f6fe843e43c835235844778aa64ce1/myWorkout/workouts"
today = datetime.now().strftime("%d/%m/%Y")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for result in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": result["name"].title(),
            "duration": result["duration_min"],
            "calories": result["nf_calories"]
            }
        }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)