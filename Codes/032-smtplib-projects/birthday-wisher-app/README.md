# Automated Birthday wish Email Sender

This Python script automates sending birthday emails to recipients listed in a CSV file. It uses `pandas` to read birthday data, `smtplib` to send emails via Gmail, and randomly selects from pre-written letter templates to personalize the messages.

## Features
- Reads birthday data from a CSV file (`birthdays.csv`).
- Checks if today matches any birthdays and sends a personalized email.
- Randomly selects one of three letter templates for variety.
- Uses Gmail's SMTP server for email delivery.
- Can be scheduled to run daily (e.g., via PythonAnywhere).

## Prerequisites
- Python 3.x installed.
- Required Python libraries:
  - `pandas`
  - `smtplib` (part of Python standard library)
  - `datetime` (part of Python standard library)
- A Gmail account with an App Password (see [Setup](#setup) for details).
- A CSV file named `birthdays.csv` with the following columns:
  - `name`: Recipient's name
  - `email`: Recipient's email address
  - `day`: Birthday day (integer)
  - `month`: Birthday month (integer)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Reza-1988/DailyCoding/Codes.git
   cd smtplib-projects/birthday-wisher-app.git
   python birthday_wisher_app.py