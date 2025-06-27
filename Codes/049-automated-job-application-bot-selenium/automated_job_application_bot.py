from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


from Codes.local_settings import LINKEDIN_DATA


# OBJECTIVE: Automate job applications on LinkedIn for "Python Developer" roles

# STEP 1: Define the LinkedIn Job Search URL
# 1. If you don't want to use your primary account for this project, feel free to set up a new email and LinkedIn account.
# 2. This is the filtered LinkedIn job search URL for "Python Developer" positions
# with the "Easy Apply" option enabled and location set to Spain.
URL = "https://www.linkedin.com/jobs/search/?currentJobId=4240382269&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

# STEP 2: Configure Selenium WebDriver for Chrome
# - Selenium uses a WebDriver to control the Chrome browser programmatically.
# - ChromeOptions is used to customize browser behavior
# - 'detach' option keeps the browser open after script execution for easier debugging
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options.
# The WebDriver acts as a bridge between our Python code and the Chrome browser.
driver = webdriver.Chrome(options=chrome_options)  # Creates a new browser session.

# Open the LinkedIn job search page in the browser.
driver.get(URL)  # Loads the LinkedIn job listings page using the filtered search URL.
time.sleep(5) # Wait for the page to load fully

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

# 3.3. Clik in Sign-in button
password_field.send_keys(Keys.ENTER)

# STEP 4: Apply to a job (Comment out this step if applying to all jobs)
# Locate the apply button and Click it
# - Note: This step is for testing a single application
time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

# If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(LINKEDIN_DATA["PHONE"])

# Locate submit button the application and click it
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()

# Step 5: Apply for all the jobs

# 5.1: Define a function to abort complex applications
# - Closes the application modal and discards the application if it requires multiple steps
def abort_application():
    # Find the close button and click it
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()
    time.sleep(2) # Wait for the discard confirmation dialog
    # Find the discard button and click it
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


# 5.2: Retrieve all job listings on the current page
# - Selects all clickable job cards using CSS selector
time.sleep(5) # Ensure job listings are fully loaded
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# 5.3: Iterate through job listings and apply to each
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Locate and Click the Aapply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(LINKEDIN_DATA["PHONE"])

        # Check if the application is simple or multi-step
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        # Check "data-control-name": It's a custom HTML attribute used by LinkedIn's frontend code.
        # These kinds of data-* attributes are commonly used for internal purposes, such as tracking user interactions.
        # The value "continue_unify" indicates that the current step is not the last one in the application form.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            # If data-control-name == "continue_unify": It means this button is a "Continue" button (i.e., more steps to come), not a one-click "Submit".
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # The application is done and Close the application modal
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    # Handle cases where the apply button or other elements are missing with Selenium Error handling modul.
    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()