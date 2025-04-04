# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACbf81ee23128bb9a3573aef31446d94a7"
auth_token = "8b515bd3096c082b2122a7cbf39ed7dd"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="It's going to rain today. remember to bring an umbrella.☂️",
    from_="+15343447977",
    to="<YOUR VERIFICATION NUMBER>",
)

print(message.status)