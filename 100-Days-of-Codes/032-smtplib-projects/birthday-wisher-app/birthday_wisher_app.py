import datetime as dt
import pandas as pd
import smtplib
import random


# READ CSV FILE AND MAKE IT DICT
birthdays_data = pd.read_csv('birthdays.csv')
birthdays_dict = birthdays_data.to_dict(orient='records')

# GET NOW DATETIME
now = dt.datetime.now()
day = now.day
month = now.month


# SET EMAIL AND PASSWORD
my_email = "<EMAIL>"
# first turn on two-step verification from https://myaccount.google.com/
# this password is coming -> https://myaccount.google.com/ -> Security -> App Password ->
# Select give your app a name e.g., Python Mail and click create. COPY THE PASSWORD -
# This is the only time you will ever see the password. It is 16 characters with no spaces.
# Use this App password in your Python code instead of your normal password.
password = "<PASSWORD>"


# CHECK IF TODAY MATCHES A BIRTHDAY IN birthdays.csv
for birthday in birthdays_dict:
    if int(birthday['day']) == day and int(birthday['month']) == month:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", 'r') as file:
            contents = file.read()
            update_contents = contents.replace("[NAME]", birthday['name'])
# SEND BIRTHDAY EMAIL
            # SMTP is stand for simple mail transfer control, it contains rules that how email can be sent around the internet.
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:  # make a new smtp object
            # TLS stand for transport layer security & it's way to securing our connection to our email server with encrypt messages.
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday['email'],
                msg=f"Subject:Happy Birthday.\n\n{update_contents}"
            )

# for running python code every day you can host the code in https://www.pythonanywhere.com/
