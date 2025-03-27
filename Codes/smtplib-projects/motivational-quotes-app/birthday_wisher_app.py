import datetime as dt
import smtplib # this is python module which allows us to use SMTP to send our email to any address in internet.
import random

# SET EMAIL AND PASSWORD
my_email = "moha.rezahosseini@gmail.com"
# first turn on two-step verification from https://myaccount.google.com/
# this password is coming -> https://myaccount.google.com/ -> Security -> App Password ->
# Select give your app a name e.g., Python Mail and click create. COPY THE PASSWORD -
# This is the only time you will ever see the password. It is 16 characters with no spaces.
# Use this App password in your Python code instead of your normal password.
password = "bpgi mrne jwem awar"

# READ QUOTES AND MAKE a RANDOM QUOTE
with open("quotes.txt", "r") as file:
    quotes_list = file.readlines()
    random_quote = random.choice(quotes_list)

# SEND QUOTE EVERY MONDAY
now = dt.datetime.now()
if now.weekday() == 0: # every Monday
    # SMTP is stand for simple mail transfer control, it contains rules that how email can be sent around the internet.
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:  # make a new smtp object
        # TLS stand for transport layer security & it's way to securing our connection to our email server with encrypt messages.
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr="moha.rezahosseini@gmail.com",
            to_addrs="physicssolar@gmail.com",
            msg=f"Subject:HELLO.\n\n{random_quote}"
        )


