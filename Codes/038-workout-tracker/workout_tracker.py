from datetime import datetime
import os
import requests


# Nutritionix API constants (personal info could be made configurable)
GENDER = "male"
WEIGHT_KG = 73
HEIGHT_CM = 173
AGE = 37
APP_ID = os.environ["NT_APP_ID"] # Nutritionix App ID
API_KEY = os.environ["NT_API_KEY"] # Nutritionix API Key

# Sheety API constants
SHEETY_ENDPOINT = os.environ["SHEET_ENDPOINT"]
SHEETY_USERNAME = os.environ['YOUR_USERNAME']
SHEETY_PASSWORD = os.environ['YOUR_PASSWORD']
SHEETY_TOKEN = os.environ["YOUR_TOKEN"]


# STEP 1- SET UP NUTRITIONIX API
# Go to the Nutritionix API website at https://www.nutritionix.com/business/api and select "Get Your API Key" to sign up for a free account.
# Double-check your spam folder (and/or your gmail "promotions" tab) for the Nutritionix verification email.
# Once logged in, you should be able to access your API key and App id:

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutritionix_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
try:
    response = requests.post(exercise_endpoint, json=nutritionix_parameters, headers=nutritionix_headers)
    response.raise_for_status()
    results = response.json()
except requests.RequestException as err:
    print(f"Nutritionix API Error: {err}")
    exit()

# STEP 2- SET UP SHEETY API
# 1- Log into Sheety with your Google Account (the same account that owns the Google Sheet you copied in step 1).
# 2- Make sure you give Sheety permission to access your Google sheets. If you miss this step, log out of Sheety and log in again.
# 3- Make sure the email matches between your Google Sheet and Sheety Account. e.g.
# 4-  In your project page, click on "New Project" and create a new project in Sheety with the name "Workout Tracking" and paste in the URL of your own "My Workouts" Google Sheet.
# 5- Click on the workouts API endpoint and enable GET and POST.

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
    # TODO: Choose one authentication method below (uncomment the desired option):
    # TODO: OPTION1: without authentication
    try:
        sheety_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)
        sheety_response.raise_for_status()
        print(sheety_response.text)
    except requests.RequestException as err:
        print(f"Sheety API Error: {err}")

# STEP 3- SET-UP AUTHENTICATION

    # TODO:OPTION2: If you set up basic Authentication use this part
    # I- Basic Authentication
    # Add either "Basic Authentication" or "Bearer Token" to your Sheety endpoint to secure it.
    # You can hardcode the token in your code for now while you test your code. Once you're sure it works.
    try:
        sheety_response = requests.post(
          SHEETY_ENDPOINT,
          json=sheet_inputs,
          auth=(
              SHEETY_USERNAME,
              SHEETY_PASSWORD,
          )
        )
        sheety_response.raise_for_status()
        print(sheety_response.text)
    except requests.RequestException as err:
        print(f"Sheety API Error: {err}")

    # TODO: OPTION 3: If you set up Token Authentication use this part
    # II- Bearer Token Authentication
    # Bearer authentication (also known as token authentication) is an HTTP authentication scheme that involves security tokens.
    # The name “Bearer authentication” basically means “give access to the bearer of this token.” The security token or “bearer token” is just a cryptic string.
    try:
        bearer_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
        }
        sheety_response = requests.post(
            SHEETY_ENDPOINT,
            json=sheet_inputs,
            headers=bearer_headers
        )
        sheety_response.raise_for_status()
        print(sheety_response.text)
    except requests.RequestException as err:
        print(f"Sheety API Error: {err}")

"""
In order to be able to post our workout data while we're out and about, it would be easier if we can access the console and run the code in a browser.
We can do this using Repl.it
This is a free tool but requires email signup. So it's completely optional if you want to do this. It's not so much for learning Python, but it would be cool to have this "app" accessible from a web browser on mobile.
Step 1 - Sign up for a free account on https://replit.com/
Step 2 - Create a new Repl and name it Google-Workouts
Step 3 - Copy and paste all your code into get_started.py on Replit.
Step 4 - However, because Repl.it projects are public, we don't want other people to see our API keys and secrets.
Add environment variables to Replit and store your Environment Variables by going into the Secrets tab and adding each environment variable as a key value pair
HINT 1: Environment variables are declared without spaces!
"""
