import os
import requests
from datetime import datetime, timedelta
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Constants for stock and company
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# API keys (using environment variables for security, with defaults for testing)
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")  # Set your api key
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")  # Set your news api key

# SETUP TWILIO
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("TWILIO_SID")  # Set your account in twilio and get your account sid
auth_token = os.environ.get("TWILIO_AUTH")  # Set you account in twilio and get your auth token
client = Client(account_sid, auth_token)

# SETUP STOCK PRICE API
# Use https://www.alphavantage.co/documentation/#daily to learn more about this API
# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries, e.g., [new_value for (key, value) in dictionary.items()]
# Replace the "demo" API key below with your own key from https://www.alphavantage.co/support/#api-key
url = f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}"
try:
    r = requests.get(url)
    r.raise_for_status()  # Check for request errors
    data = r.json()['Time Series (Daily)']
except requests.RequestException as e:
    print(f"Error fetching stock data: {e}")
    exit()

# Calculate yesterday's date
yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
try:
    # Fetch yesterday's closing price directly from the data
    yesterday_price = float(data[yesterday]['4. close'])
except KeyError:
    print("We don't have yesterday's data")
    exit()

# Get the day before yesterday's closing stock price
before_yesterday = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')
try:
    # Fetch the day before yesterday's closing price directly
    before_yesterday_price = float(data[before_yesterday]['4. close'])
except KeyError:
    print("We don't have data for the day before yesterday")
    exit()

# Find the positive difference between yesterday's close price and the day before yesterday's close price
difference = float(yesterday_price) - float(before_yesterday_price)
up_down = "🔺" if difference > 0 else "🔻"

# Work out the percentage difference in price between yesterday's closing price and the closing price from the day before yesterday
diff_percent = round((difference / float(before_yesterday_price)) * 100)

# SETUP NEWS API
# If diff percentage is greater than 5, then get news
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Get the first 3 news pieces for the COMPANY_NAME
    three_articles = articles[:3]

    # Create a new list of the first 3 articles' headlines and descriptions using list comprehension
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in three_articles
    ]

    # Send each article as a separate message via Twilio
    for formatted_article in formatted_articles:
        message = client.messages.create(
            body= formatted_article,
            from_= "<Your Twilio Number>",
            to= "<YOUR VERIFICATION NUMBER>",
        )
        print(f"Message status: {message.status}")
else:
    print(f"Price change ({diff_percent}%) is below 5%, no news fetched.")
