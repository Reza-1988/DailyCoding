import time
import requests
from datetime import datetime
import smtplib


MY_EMAIL = "<EMAIL>" # Set your email address
MY_PASSWORD = "<PASSWORD>" # set the password with this instruction ->
# first turn on two-step verification from https://myaccount.google.com/
# this password is coming -> https://myaccount.google.com/ -> Security -> App Password ->
# Select give your app a name e.g., Python Mail and click create. COPY THE PASSWORD -
# This is the only time you will ever see the password. It is 16 characters with no spaces.
# Use this App password in your Python code instead of your normal password.
MY_LAT = 41.385063 # Your latitude
MY_LONG = 2.173404 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LAT+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# This code every 60 seconds check the conditions and if are True send you email to be aware
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:  # make a new smtp object
            # TLS stand for transport layer security & it's way to securing our connection to our email server with encrypt messages.
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look Up.\n\nThe ISS is above you in the sky."
            )
