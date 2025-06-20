# Rain Alert App

This is a simple Python application that checks the weather forecast for the next 12 hours using the OpenWeatherMap API and sends an SMS alert via Twilio if rain is expected.

## Project Files
- **`rain_alert_app.py`**: The main script that fetches weather data and determines if rain is expected.
- **`send_sms.py`**: A module that handles sending SMS notifications using Twilio.

## Features
- Fetches a 12-hour weather forecast from OpenWeatherMap API.
- Analyzes weather condition IDs to detect precipitation (rain or snow).
- Sends an SMS alert if rain is predicted, reminding the user to bring an umbrella.

## Prerequisites
Before running the application, ensure you have the following:
1. **Python 3.x** installed.
2. Required Python libraries:
   - `requests`: For making API calls.
   - `twilio`: For sending SMS notifications.
3. An **OpenWeatherMap API key** (sign up at [openweathermap.org](https://openweathermap.org/)).
4. A **Twilio account** with an Account SID, Auth Token, and a Twilio phone number (sign up at [twilio.com](https://twilio.com/)).

## Installation
1. **Clone or download this project** to your local machine.
2. **Install dependencies**:
   Open a terminal in your project directory and run:
   ```bash
   pip install requests twilio
   git clone https://github.com/Reza-1988/DailyCoding/Codes.git
   cd rain-alert-app.git
   python rain_alert_app.py