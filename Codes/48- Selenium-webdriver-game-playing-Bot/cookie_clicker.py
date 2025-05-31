import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
we're going to be introducing a new technology for advanced web scraping,and that is Selenium WebDriver.
Now you might have heard of Selenium WebDriver before because it's probably one of the most well-known automation and testing tools
for web developers out there. But you might be wondering, well, we already have Beautiful Soup. So why do we need to learn a new technology?
Well, one of the things that we've really been limited by is we can't actually use all the capabilities that browsers can do.
So when we load up a website with beautiful soup, we can't, for example, type something into the website and then click on something. And to create these
chains of continuous actions where we basically automate the entire flow of a particular job or a particular task. To do that,
we're going to need to use Selenium WebDriver. Now, this is a free tool and it basically allows us to automate the browser, get the browser to do things automatically
depending on a script or a piece of code that we write. Now, this is going to enable us to type as well as click as well as scroll.
Basically anything that a human pretty much can do on a website, you can do using a Selenium driven browser.
It's kind of like we're building a robot and telling it what to do on a browser. And selenium is the tool that allows the robot to interact and communicate with the browser.
"""

# OBJECTIVE: Build an automated bot to play the Cookie Clicker game
# This script uses Selenium (a tool for automating web browsers) and Python to play the Cookie Clicker game.
# The bot's goal is to click the cookie as fast as possible to earn cookies (the game's currency).
# Every 5 seconds, it checks the right-hand panel for upgrades (like hiring grandmas or factories) that it can afford.
# It then buys the most expensive upgrade it can afford to maximize cookie production efficiency.
# The bot compares the number of cookies it has with the prices of upgrades to make smart purchasing decisions.

# STEP 1: Define the URL of the Cookie Clicker game
# This is the website where the game is hosted.
URL = "https://orteil.dashnet.org/experiments/cookie/"

# STEP 2: Configure the Chrome browser to stay open and set up Selenium
# Selenium uses a WebDriver to control the Chrome browser programmatically.
# We use ChromeOptions to customize browser behavior.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # This keeps the browser open after the script finishes, useful for debugging if something goes wrong.

# Initialize the Chrome WebDriver with the specified options.
# The WebDriver acts as a bridge between our Python code and the Chrome browser.
driver = webdriver.Chrome(options=chrome_options)  # Creates a new browser session.

# Open the Cookie Clicker website in the browser.
driver.get(URL)  # Loads the game page in the browser.

# STEP 3: Locate the cookie button on the webpage
# The cookie is the main element we click to earn cookies.
# We use its ID ("cookie") to find it on the page.
cookies_button = driver.find_element(By.ID, value="cookie")  # Stores the cookie button element for repeated clicking.

# STEP 4: Collect all upgrade items and their prices from the right-hand panel
# The right-hand panel contains upgrades (e.g., Cursor, Grandma) that we can buy to improve cookie production.
# Each upgrade is inside a <div> element in the "store" section of the page.
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")  # Gets all <div> elements in the store.
item_ids = [item.get_attribute("id") for item in items]  # Extracts the unique ID of each upgrade item.


# STEP 5: Define a function to check cookies and buy the most expensive affordable upgrade
# This function runs every 5 seconds to decide which upgrade to purchase.
def purchase(store_items):
    # 1. Get the current number of cookies.
    # The cookie count is displayed in an element with ID "money".
    money_element = driver.find_element(By.ID, value="money").text  # Fetches the current cookie count.
    if "," in money_element:  # Large numbers (e.g., 1,000) include commas, which we need to remove.
        money_element = money_element.replace(",", "")
    cookie_count = int(money_element)  # Convert the cookie count to an integer.

    # 2. # Step 2: Retrieve the price for each upgrade element and store the data in a dictionary,
    # mapping each item name to its corresponding price.
    # IMPORTANT: You must fetch the prices inside the loop, not outside it.
    # This is because each time you purchase an upgrade, the price of that upgrade increases.
    # If you only get the prices once (before the loop), you will be using outdated values,
    # which can cause incorrect purchasing decisions or errors.

    # Get the prices of upgrades, which are displayed in <b> tags within the store.
    all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")  # Finds all price elements.
    item_prices = []
    # Loop through each price element to extract the numerical cost.
    for price in all_prices:
        element_text = price.text  # Get the text of the price element (e.g., "Cursor - 15").
        if element_text != "":  # Skip empty elements (some <b> tags may be empty).
            # Extract the price part after the dash (e.g., "15" from "Cursor - 15").
            # Remove commas (e.g., "1,000" becomes "1000") and convert to an integer.
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_prices.append(cost)

    # Create a dictionary to map prices to upgrade IDs.
    # This helps us quickly look up which upgrade to buy based on its cost.
    store_dict = {}
    for i in range(len(item_prices)):
        store_dict[item_prices[i]] = item_ids[i]  # Maps each price to its corresponding upgrade ID.

    # 3. Create a dictionary of upgrades we can afford.
    # We check which upgrades have a price less than or equal to our current cookie count.
    items_we_can_buy = {}
    for cost, item_id in store_dict.items():
        if cookie_count >= cost:  # If we have enough cookies, add the upgrade to the dictionary.
            items_we_can_buy[cost] = item_id

    # 4. If we can afford any upgrades, buy the most expensive one.
    # The most expensive affordable upgrade typically provides the best boost to cookie production.
    if items_we_can_buy:  # Check if there are any affordable upgrades.
        highest_cost = max(items_we_can_buy)  # Find the highest price we can afford.
        highest_item_id = items_we_can_buy[highest_cost]  # Get the ID of that upgrade.

        # 5. Click the upgrade to purchase it.
        # We use the driver to find and click the element, as the page updates dynamically after each purchase.
        driver.find_element(by=By.ID, value=highest_item_id).click()
    else:
        print("No affordable upgrades at this time.")  # Inform if no upgrades can be bought.

# STEP 6: Set up timing for checking upgrades and stopping the bot
# We check for upgrades every 5 seconds and stop the bot after 5 minutes.
upgrade = time.time() + 5  # Schedule the first upgrade check 5 seconds from now.
five_min = time.time() + 60 * 5  # Set the bot to run for 5 minutes (300 seconds).

# STEP 7: Run the main game loop
# The bot clicks the cookie continuously and checks for upgrades every 5 seconds.
while True:
    cookies_button.click()  # Click the cookie to earn more cookies.

    # Check if it's time to look for upgrades (every 5 seconds).
    if time.time() > upgrade:
        print("Checking for upgrades...")  # Notify that we're checking upgrades.
        purchase(item_ids)  # Call the purchase function to buy an upgrade.
        upgrade = time.time() + 5  # Schedule the next upgrade check.

    # STEP 8: Stop the bot after 5 minutes and display cookies per second
    # After 5 minutes, we check the cookies-per-second rate to see how efficient the bot was.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text  # Get the cookies-per-second value.
        print(f"Cookies per second: {cookie_per_s}")  # Print the final rate.
        break  # Exit the loop to stop the bot.