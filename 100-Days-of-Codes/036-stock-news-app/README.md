# Stock Price Alert App

This Python application monitors the daily stock price of Tesla (TSLA), calculates the percentage change between yesterday and the day before, and sends SMS alerts with relevant news if the change exceeds 5%. It uses the Alpha Vantage API for stock data, NewsAPI for news, and Twilio for SMS notifications.

## Features
- Fetches daily closing stock prices for Tesla (TSLA) using Alpha Vantage.
- Calculates the percentage difference between yesterday’s and the day before yesterday’s closing prices.
- Retrieves the latest news about Tesla Inc from NewsAPI if the price change is greater than 5%.
- Sends SMS alerts via Twilio with stock change details and news headlines.

## Project Files
- **`stock_alert.py`**: The main script handling stock price retrieval, percentage calculation, news fetching, and SMS sending.

## Prerequisites
- **Python 3.x** installed.
- Required libraries:
  - `requests`: For API calls.
  - `twilio`: For SMS notifications.
- API keys and credentials:
  - [Alpha Vantage API key](https://www.alphavantage.co/support/#api-key).
  - [NewsAPI key](https://newsapi.org/).
  - [Twilio Account SID, Auth Token, and phone number](https://twilio.com/console).

## Installation
1. **Clone or download this repository** to your local machine.
2. **Install dependencies**:
   ```bash
   pip install requests twilio
   git clone https://github.com/Reza-1988/DailyCoding/Codes.git
   cd stock-news-app.git
   python stock_news_app.py