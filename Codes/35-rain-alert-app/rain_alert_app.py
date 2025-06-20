import requests
import send_sms


# To access the weather API, visit this website: https://openweathermap.org/
# Create your own account and generate an API key.
# This API endpoint provides a 5-day weather forecast.
# Before using the API, ensure you thoroughly read the documentation first; avoid rushing into work without understanding it.
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "b1b665b85f395f733862a12d15444ba1" # you must make your API key this doesn't work you!
parameters = {
    "lat": 41.385063, # You can obtain your latitude and longitude from this website: https://www.latlong.net/
    "lon": 2.173404,
    "appid": api_key,
# The 'cnt' parameter stands for count. By setting it to 4, we request only four timestamps,
# covering a 12-hour window relevant to our needs.
    "cnt": 4,
}

response = requests.get(OWM_Endpoint , params=parameters)
response.raise_for_status()
# To explore JSON data, you can copy and paste it into https://jsonviewer.stack.hu/
# for a clearer and more structured view.
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    weather_condition_id = hour_data['weather'][0]['id']
    # In the API documentation, the 'id' represents weather conditions.
    # If the id is less than 700, it indicates precipitation such as rain or snow.
    if int(weather_condition_id) < 700:
        will_rain = True

if will_rain:
    my_message = send_sms.message
