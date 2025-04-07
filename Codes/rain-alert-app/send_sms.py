# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("api_key")
auth_token = os.environ.get("auth_token")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="It's going to rain today. remember to bring an umbrella.☂️",
    from_="<Your Twilio Number>",
    to="<YOUR VERIFICATION NUMBER>",
)

print(message.status)
