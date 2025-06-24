import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "lxml")

titles = [title.text for title in soup.find_all(name="h3", class_="title")]

with open("movies.txt", "w") as file:
    for i in range(len(titles)-1, -1, -1):
        file.write(f"{titles[i]}\n")
