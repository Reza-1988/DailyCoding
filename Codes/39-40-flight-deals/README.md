# Flight Deals Finder

The **Flight Deals Finder** is a Python-based application that searches for affordable flight deals from a specified 
origin (e.g., London, `LON`) to various destinations listed in a Google Sheet. It uses the Amadeus API to fetch flight data, 
the Sheety API to manage destination and customer data, Twilio for SMS notifications, and SMTP for email notifications. 
When a flight’s price is below the target price in the Google Sheet, the system notifies users via email and sends 
an SMS to the project owner.

## Features
- Retrieves destination data and customer information from Google Sheets using the Sheety API.
- Fetches IATA codes for cities and searches for direct and indirect flights using the Amadeus API.
- Identifies the cheapest flights for each destination within a specified date range (next day to six months).
- Sends SMS notifications (via Twilio) and email alerts (via SMTP) when low-price flights are found.
- Supports both direct and indirect flight searches if direct flights are unavailable or too expensive.

## Project Structure
- `__init__.py`: Empty file to make the project a Python package; included due to `local_settings.py` in the outer directory.
- `data_manager.py`: Manages interactions with Google Sheets via the Sheety API to retrieve and update destination and customer data.
- `flight_data.py`: Defines the `FlightData` class and a function to find the cheapest flight from Amadeus API data.
- `flight_search.py`: Handles Amadeus API interactions to retrieve IATA codes and search for flights.
- `flight_deals_main.py`: Main script that orchestrates the flight search, data management, and notifications.
- `notification_manager.py`: Manages SMS (Twilio) and email (SMTP) notifications for low-price flight alerts.
- `sample_settings.py`: Sample configuration file for API keys and credentials (actual `local_settings.py` is in `.gitignore`).

## Prerequisites
- Python 3.8 or higher
- A Google Sheet with destination data (city, IATA code, lowest price, ID) and customer data (first name, last name, email)
- Accounts and API credentials for:
  - [Amadeus API](https://developers.amadeus.com/) (for flight data)
  - [Sheety API](https://sheety.co/) (for Google Sheet integration)
  - [Twilio](https://www.twilio.com/) (for SMS notifications)
  - SMTP server (e.g., Gmail with an App Password for email notifications)


## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Reza-1988/DailyCoding/Codes.git
   cd flight-deals
   pip install requests twilio smtplib
   ```
   
2. **Set Up a Virtual Environment (recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install Dependencies**: Install the required Python packages listed in requirements.txt (create one if not present):
    ```bash
    pip install requests twilio smtplib
   ```

4. **Configure Settings**:
   - Copy sample_settings.py to local_settings.py in the parent directory of the project:
     - Note: `local_settings.py` is ignored by `.gitignore` to protect sensitive information.

5. **Set Up Google Sheets**:
   - Create a Google Sheet for destinations with columns: city, iataCode, lowestPrice, id.
   - Create a Google Sheet for customers (e.g., via a Google Form) with columns: firstName, lastName, whatIsYourEmail?.
   - Link these sheets to Sheety to get API endpoints.