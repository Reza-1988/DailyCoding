import requests


URL =  "https://quera.org/college/3078/chapter/9356/lesson/31131/?comments_page=1&comments_filter=ALL"
"https://quera.org/college/3078/chapter/9356/lesson/31131/"
params = {"comments_page": 1, "comments_filter": "ALL"}

response = requests.get(URL)

print(response.status_code)

print(response.text)