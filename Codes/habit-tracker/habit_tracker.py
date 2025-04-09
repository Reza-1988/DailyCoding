import os

import requests

USERNAME = "reza-1988"  # os.environ['USERNAME']
TOKEN = "somthing_token"  # os.environ['TOKEN']



#  STEP1- MAKE YOUR USERNAME
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# hit first time for this part for make your valid username
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# STEP2- MAKE YOUR GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/a-know/graphs"

graph_config = {
    "id": "graph1", # Be careful that number not allowed in first of id
    "name": "Thinking Graph",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
}

