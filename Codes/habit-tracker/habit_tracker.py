import os
import requests
from datetime import datetime

# User credentials (use environment variables for security)
USERNAME = os.environ.get("PIXELA_USERNAME", "reza-1988")
TOKEN = os.environ.get("PIXELA_TOKEN", "somthing_token")

# Base Pixela API endpoint
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# Authentication header required for most Pixela requests
HEADERS = {"X-USER-TOKEN": TOKEN}

# STEP 1: Create a Pixela user account
# Visit https://pixe.la/ to learn more about the API
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment and run this section only once to register your username
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# STEP 2: Create a habit tracking graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",  # Note: IDs must not start with a number
    "name": "Thinking Graph",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"  # See Pixela docs for color options
}

# Uncomment and run this section once to create your graph
# From the documentation: The 'X-USER-TOKEN' header is required for authentication
# response = requests.post(graph_endpoint, json=graph_config, headers=HEADERS)
# print(response.text)

# STEP 3: Post a pixel to track today's habit
pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.today().strftime("%Y%m%d")  # Format: YYYYMMDD
pixel_data = {
    "date": today,
    "quantity": input("How many minutes did you spend deep thinking today? ")
}

try:
    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=HEADERS)
    response.raise_for_status()
    print(response.text)
except requests.RequestException as e:
    print(f"Error posting pixel: {e}")

# STEP 4: Update an existing pixel
update_pixel_date = today  # You can specify a different date to update a past pixel
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}/{update_pixel_date}"

update_pixel_data = {
    "quantity": "90"  # New value in minutes
}

# Uncomment to update the pixel for the specified date
# response = requests.put(update_endpoint, json=update_pixel_data, headers=HEADERS)
# print(response.text)

# STEP 5: Delete a pixel
delete_pixel_date = today  # You can change this to delete a specific date's pixel
delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}/{delete_pixel_date}"

try:
    response = requests.delete(delete_endpoint, headers=HEADERS)
    response.raise_for_status()
    print(response.text)
except requests.RequestException as e:
    print(f"Error deleting pixel: {e}")