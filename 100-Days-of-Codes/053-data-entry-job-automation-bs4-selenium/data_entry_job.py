from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from pprint import pprint

# OBJECTIVE: Automate a data entry job for real estate listings

# STEP 1: Define the static Zillow clone URL and scrape it using BeautifulSoup
URL = "https://appbrewery.github.io/Zillow-Clone"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")



# Extract property prices
# This selects all <span> elements with the specific class containing price info
price_element = soup.select('.PropertyCardWrapper .PropertyCardWrapper__StyledPriceLine')
for price in price_element:
    print(price.getText(strip=True))

# Extract property links
# find_all methode means here:
# - Only return all <a> tags that have a data-test attribute with the value 'property-card-link'.
url_element = soup.find_all('a', attrs={'data-test': 'property-card-link'})
for tag in url_element:
    print(tag.get('href'))

# Get address of each property
# find_all methode means here:
# - Only return all <address> tags that have a data-test attribute with the value 'property-card-addr'.
address_element = soup.find_all('address', attrs={'data-test':'property-card-addr'})
for tag in address_element:
    print(tag.get_text(strip=True))













# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(URL)


