# ISS Overhead Notifier

This Python script monitors the International Space Station (ISS) position and sends an email notification when the ISS is overhead your location during nighttime.

## Features
- Uses the Open Notify API to track the ISS's current position.
- Checks sunrise and sunset times via the Sunrise-Sunset API to determine if it's nighttime.
- Sends an email alert using Gmail's SMTP server when the ISS is within ±5 degrees of your latitude and longitude during the night.
- Runs continuously, checking every 60 seconds.

## Prerequisites
- Python 3.x installed.
- Required Python libraries:
  - `requests`
  - `smtplib` (part of Python standard library)
  - `datetime` (part of Python standard library)
  - `time` (part of Python standard library)
- A Gmail account with an App Password (see [Setup](#setup)).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Reza-1988/DailyCoding/Codes.git
   cd requests-lib-projects/iss-overhead-api.git
   python iss_overhead.py