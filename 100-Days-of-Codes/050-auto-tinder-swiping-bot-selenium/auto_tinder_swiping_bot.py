from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from Codes.local_settings import TINDER_DATA

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


# STEP 3: Navigate to login page
time.sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="q-407077530"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()

time.sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="q-2135458606"]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
fb_login.click()


# STEP 4: Login with Facebook
# 4.1. Switch to the Facebook login window
# The Facebook login page opens in a new window. We have to switch to new windows for selenium to work on it.
time.sleep(2)
base_window = driver.window_handles[0] # Get Tinder window identification handle
fb_login_window = driver.window_handles[1] # Get Facebook window identification handle
driver.switch_to.window(fb_login_window)
print(driver.title) # If title print out "Facebook": process is fine.

#4.2 Accept cookies
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div/span/span').click()

# 4.3 Fill in email and password fields for Facebook login
time.sleep(2)
fb_email = driver.find_element(By.ID, "email")
fb_email.send_keys(TINDER_DATA["EMAIL"])
fb_password = driver.find_element(By.ID, "pass")
fb_password.send_keys(TINDER_DATA["PASSWORD"])
fb_password.send_keys(Keys.ENTER)

# 4.4 Switch back to Tinder window
time.sleep(2)
driver.switch_to.window(base_window)
print(driver.title)