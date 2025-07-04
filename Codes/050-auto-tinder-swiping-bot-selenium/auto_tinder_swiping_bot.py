from selenium import webdriver
from selenium.webdriver.common.by import By

import time


# OBJECTIVE: Build Auto Tinder Swiping Bot


# STEP 1: Define the Tinder URL and Configure Selenium WebDriver for Chrome
URL = "https://tinder.com"

# Customize driver with ChromeOption
# 'detach' option keeps the browser open after script execution for easier debugging
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Creates a new browser session
driver = webdriver.Chrome(options=chrome_options)

# Open Tinder url with webdriver
driver.get(URL)
time.sleep(2)

# STEP 3: Navigate to login page
login_button = driver.find_element(By.XPATH, '//*[@id="q-407077530"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()
time.sleep(2)

