import requests

URL = "http://127.0.0.1:8000/"

def add_book(book: dict[str, str]) -> str or None:
    category = book["category"]
    if category not in ["mathematics", "physics", "chess" ]:
        return "Invalid Category"

    url = f"{URL}{category}/"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "Bad Request"
    except requests.exceptions.RequestException:
        return "Bad Request"


    data = response.json()
    for item in data:
        if item["name"] == book["name"]:
            return "Bad Request"

    try:
        post_response = requests.post(url, json=book)
        if post_response.status_code != 201:
            return None
        else:
            return "Bad Request"
    except requests.exceptions.RequestException:
        return "Bad Request"

