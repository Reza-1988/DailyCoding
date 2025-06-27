from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


from Codes.local_settings import LINKEDIN_DATA


# OBJECTIVE: Build an automated job application bot

# STEP 1: Define the URL for the LinkedIn Job Search
# 1. If you don't want to use your primary account for this project, feel free to set up a new email and LinkedIn account.
# 2. This is the filtered LinkedIn job search URL for "Python Developer" positions
# with the "Easy Apply" option enabled and location set to Spain.
URL = "https://www.linkedin.com/jobs/search/?currentJobId=4240382269&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

# STEP 2: Configure the Chrome browser to stay open and set up Selenium
# Selenium uses a WebDriver to control the Chrome browser programmatically.
# We use ChromeOptions to customize browser behavior.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) # This keeps the browser open after the script finishes, useful for debugging if something goes wrong.

# Initialize the Chrome WebDriver with the specified options.
# The WebDriver acts as a bridge between our Python code and the Chrome browser.
driver = webdriver.Chrome(options=chrome_options)  # Creates a new browser session.

# Open the LinkedIn job search page in the browser.
driver.get(URL)  # Loads the LinkedIn job listings page using the filtered search URL.
time.sleep(5)

# STEP 3: Automatically Login

# 3.1: Navigate to the Sign-In page
# When the LinkedIn job search page loads, a prompt may appear asking you how you'd like to sign in
# (e.g., "Sign in with email", "Continue with Google", etc.).
# This block checks for the button that takes you directly to the email/password sign-in page.
try:
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    sign_in_button.click()
except Exception as e:
    print("Sign-in button not found or already on login page:", e)


# 3.2. Locate username(Email Or phone) and password fields in the Sign-In page and fill them.
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_key")
email_field.send_keys(LINKEDIN_DATA["EMAIL"])
password_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_password")
password_field.send_keys(LINKEDIN_DATA["PASSWORD"])

# 3.3. Clik in SignIn button
password_field.send_keys(Keys.ENTER)

# STEP 4: Apply for a Job

# 4.1. Locate the apply button and Click it
time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

# 4.2. If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(LINKEDIN_DATA["PHONE"])

#4.3. Locate submit button the application and click it
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()