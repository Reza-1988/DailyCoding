# Workout Tracking App

This Python script helps you track your workouts by integrating with the **Nutritionix API** to analyze exercises and the **Sheety API** to log the data into a Google Sheet. It’s perfect for anyone who wants to record their fitness progress automatically, including exercise names, duration, calories burned, and timestamps.

## Features
- **Exercise Parsing:** Enter natural language input (e.g., "30 min yoga, 2 miles running") and get detailed stats from Nutritionix.
- **Automated Logging:** Saves your workout data to a Google Sheet with the current date and time.
- **Flexible Authentication:** Supports three ways to secure your Sheety API (no auth, Basic Auth, or Bearer Token).
- **Error Handling:** Includes basic error checking for API requests.

## Prerequisites
- **Python 3.x:** Ensure you have Python installed (check with `python --version` or `python3 --version`).
- **Google Account:** Needed for Google Sheets and Sheety integration.
- **API Accounts:** Sign up for Nutritionix and Sheety to get your API keys.
- **Internet Connection:** Required for API calls.

## Setup Instructions

### 1. Clone or Download the Project

```bash
   git clone https://github.com/Reza-1988/DailyCoding/Codes.git
   cd workout_tracker.git
   python workout_tracker.py