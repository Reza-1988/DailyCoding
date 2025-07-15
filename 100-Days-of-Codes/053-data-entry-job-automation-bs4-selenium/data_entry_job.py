from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# OBJECTIVE: Automate a data entry job for real estate listings

# STEP 1: Define the static Zillow clone URL and scrape it using BeautifulSoup
URL = "https://appbrewery.github.io/Zillow-Clone"
GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSf-SZ-2wFaPSbb3o85n44rajNNhMRPc3e9mA0brDLH-M2DmTw/viewform?usp=dialog"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

# STEP 2: Scrape Property Data Using BeautifulSoup

# 1.2: CExtract and Create a list of all the prices on the page using a CSS Selector
# This selects all <span> elements with the specific class containing price info
# Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
all_prices = soup.select('.PropertyCardWrapper .PropertyCardWrapper__StyledPriceLine')
prices_list = []
for price in all_prices:
   x = re.search(r'\$\d[\d,]*',  price.get_text(strip=True)).group()
   prices_list.append(x)


# 1.2: Extract and Create a list of all the links on the page using find_all methode means here:
# - Only return all <a> tags that have a data-test attribute with the value 'property-card-link'.
all_links = soup.find_all('a', attrs={'data-test': 'property-card-link'})
links_list = [url.get('href') for url in all_links]


# 1.3: Extract and Create a list of all the addresses with find_all methode means here:
# Only return all <address> tags that have a data-test attribute with the value 'property-card-addr'.
# Remove newlines \n, pipe symbols |, and whitespaces to clean up the address data
all_addresses = soup.find_all('address', attrs={'data-test': 'property-card-addr'})
addresses_list = [address. get_text(strip=True).replace("|", " ") for address in all_addresses]

# TODO: STEP 4: Set up your Google form and add Google form link in top

# STEP 5: Fill Out Data in the Google Form Using Selenium

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


# all inputs are inside of Class name "whsOnd", get all inputs with find_elements in a list after that going through each input with index
inputs = driver.find_elements(By.CLASS_NAME, "whsOnd")

# Loop through each listing and fill out the form with its data and submit the form
for i in range (len(links_list)):
    # TODO: Add fill in the link to your own Google From
    driver.get(GOOGLE_FORM_LINK)
    time.sleep(2)
    # All form inputs are inside of Class name "whsOnd", get all inputs with find_elements in a list after that going through each input with index
    inputs = driver.find_elements(By.CLASS_NAME, "whsOnd")
    submit_button = driver.find_element(By.CLASS_NAME, "NPEfkd") # get the submit button

    inputs[0].send_keys(addresses_list[0]) # First input that we define in google form is address
    inputs[1].send_keys(prices_list[0]) # Second input that we define in google form is price
    inputs[2].send_keys(links_list[0]) # Third input that we define in google form is link
    submit_button.click()


