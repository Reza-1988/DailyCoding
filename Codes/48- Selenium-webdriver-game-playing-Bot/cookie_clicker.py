import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Step 1: Set up URL
URL = "https://orteil.dashnet.org/experiments/cookie/"

# Step 2: Set up WebDriver and ChromeOptions to keep the browser open after the script ends

# Configure Chrome to remain open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# ChromeDriver acts as a bridge between Selenium and the Chrome browser
# Start the Chrome browser with the specified options
driver = webdriver.Chrome(options=chrome_options) # Initializing a new Chrome WebDriver object

# Navigate to the desired webpage
driver.get(URL)  # Replace 'URL' with the actual URL you want to open

# Step 3: Create a bot using Selenium and Python to click on the cookie as fast as possible.
cookies_button = driver.find_element(By.ID, value="cookie")


# Step 4: Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive one.
# You'll need to check how much money (cookies) you have against the price of each upgrade.


start_time = time.time()
upgrade = start_time + 5
while time.time() - start_time < 300:
    cookies_button.click()
    if time.time() >= upgrade:

        money = driver.find_element(By.ID, value="money") # Update money every loop
        money_amount = int(money.text)
        cookies_button.click()

        if int(money_amount) > 15:
            cursor = driver.find_element(By.ID, value="buyCursor")  # <-- re-find element here
            cursor.click()
            time.sleep(0.1)

        upgrade = time.time() + 5

