from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
from ..local_settings import TINDER_DATA

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

# 4.3 Fill in email and password fields for Facebook login and hit enter
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

# STEP 5: Dismiss all requests

#Delay by 5 seconds to allow page to load.
time.sleep(5)

#Allow location
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# STEP 6: Hit Like!

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1-second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
