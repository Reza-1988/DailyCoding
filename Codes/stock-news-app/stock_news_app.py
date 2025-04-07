import os

import requests
from datetime import datetime, timedelta
from newsapi import NewsApiClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "7OAUKXQGVKQ0O078" #os.environ.get("STOCK_API_KEY")


# Use https://www.alphavantage.co/documentation/#daily
# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}"
r = requests.get(url)
data = r.json()['Time Series (Daily)']
yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

try:
    for item in data.items():
        if yesterday == item[0]:
            yesterday_price = item[1]['4. close']
except KeyError:
    print("we don't have yesterday data")


# Get the day before yesterday's closing stock price
before_yesterday = (datetime.today() - timedelta(days=2)).strftime('%Y-%m-%d')
try:
    for item in data.items():
        if before_yesterday == item[0]:
            before_yesterday_price = item[1]['4. close']
except KeyError:
    print("we don't have before yesterday data")

# Find the positive difference between yesterday close price and before yesterday close price.
difference = abs(float(yesterday_price) - float(before_yesterday_price))


# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_difference = (difference / float(before_yesterday_price)) * 100
print(percentage_difference)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

# if 11 > 10:
#     response_news = requests.get(NEWS_ENDPOINT)
#     newsapi = NewsApiClient(api_key='c9dc213929de4f88bcf44bb1a1760649')
#     top_headlines = newsapi.get_everything(q='tesla')
#     print(top_headlines)
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

