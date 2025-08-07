import requests

def find_category(url: str) -> str:

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        return "Bad Request"

    if response.status_code != 200:
        return "Bad Request"

    try:
        data = response.json()
    except ValueError:
        return "Bad Request"

    if not data:
        return "I can't recognize it"

    if not isinstance(data, list):
        return "I can't recognize it"

    first_category = data[0].get("category")
    if not first_category:
        return "I can't recognize it"
    flag = True
    for book in data:
        if first_category != book.get("category"):
            flag = False
    if not flag:
        return "I can't recognize it"
    return first_category





