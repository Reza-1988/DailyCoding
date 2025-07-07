import requests
from bs4 import BeautifulSoup


# STEP 1 - prompt that asks what year you would like to travel to.
hot_year = input("Which year do yo want to travel to? Type the date in this format YYY-MM-DD: ")


# STEP 2 - Build the Billboard URL using the year (and date) entered by the user
url = "https://www.billboard.com/charts/hot-100/" + hot_year + "/"

## STEP 3 - Define a header to make the request look like it's coming from a real browser
# This helps avoid being blocked while scraping the destination URL


# The 'User-Agent' is an HTTP header that tells the server what kind of client is making the request.
# It usually includes information about the browser, operating system, and device type.
# Some websites (like Billboard) may block or restrict access if they detect that the request is not
# coming from a regular web browser (like Firefox or Chrome).
# By setting a User-Agent string that mimics a real browser (e.g., Firefox), we help make our request
# look more like it's coming from a normal user and not an automated script.
# This helps us avoid getting blocked or receiving incomplete data.
# for more information check here https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
# Breakdown of the User-Agent string:
# "Mozilla/5.0"       → Common prefix used by most browsers for compatibility.
# "(Windows NT 10.0; Win64; x64)" → OS info: Windows 10, 64-bit version.
# "rv:131.0"          → Firefox version (rendering engine version).
# "Gecko/20100101"    → Gecko is the engine behind Firefox; this part is usually fixed.
# "Firefox/131.0"     → The actual browser and version number.


# STEP 4 - Send a GET request to the URL using the requests library
# This retrieves the web page content for scraping
response = requests.get(url, headers=headers)
response.raise_for_status()

# STEP 5 - Parse the HTML content using BeautifulSoup and extract song title elements
soup = BeautifulSoup(response.text, 'lxml')  # Create a BeautifulSoup object to navigate the HTML
song_names_spans = soup.select("li ul li h3")  # Use CSS selector to find all <h3> tags within the chart list

# We use soup.select() to extract specific elements from the HTML using CSS selectors.
# CSS selectors are patterns used to select HTML elements, just like in web design (CSS).
# In this case: "li ul li h3" means:
#   - Find all <h3> tags
#   - That are inside a <li>
#   - That is inside a <ul>
#   - That is itself inside another <li>
# This matches the structure of the Billboard chart page, where each song name is inside an <h3> tag
# deeply nested in <li> and <ul> tags.
# The result is a list of all matching <h3> tags (song titles).

# Why is it called a "CSS selector"?
# Because it uses the same syntax as Cascading Style Sheets (CSS),
# which web developers use to select and style elements on a web page.
# For example:
#   - "h3" selects all <h3> tags
#   - ".title" selects elements with class="title"
#   - "div > p" selects <p> tags directly inside a <div>
# In web scraping, we reuse this CSS-style syntax to find and extract elements
# from the HTML page using BeautifulSoup's select() function.
# This makes it easy and powerful, especially if you're already familiar with web design or HTML.

# STEP 6 - Loop through all the <h3> tags and extract the song names as plain text
song_names = [song.getText().strip() for song in song_names_spans]


