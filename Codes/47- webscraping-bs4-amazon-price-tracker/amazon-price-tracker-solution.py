import requests
from bs4 import BeautifulSoup
import smtplib
from Codes.local_settings import SMTP_DATA

# Step 1: Set up target price and product URL
BUY_PRICE = 100 # Set the price below which you would like to get a notification
practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Step 2: Fetch the webpage
response = requests.get(practice_url)

# Step 3: Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# Step 4: Extract the price
# Extract the product price from the HTML content.
# It finds the first element with class 'a-offscreen' that is nested inside an element with class 'a-price'.
# This specific span usually contains the full price (e.g., $99.99) in a clean, accessible format.
# Then, .getText() retrieves the visible text from that HTML tag.
price = soup.select_one(".a-price .a-offscreen").getText()
price_float = float(price.strip().replace("$", ""))# Remove dollar sign and + Convert to float


# Step 5: Extract the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)


# Step 6: Check if price is below target and send email
if price_float < BUY_PRICE:
    message = f"{title} is on sale for ${price_float}!"

    # Compose the email and Send the email using SMTP
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:  # make a new smtp object
            # TLS stand for transport layer security & it's way to securing our connection to our email server with encrypt messages.
            connection.starttls()
            connection.login(user=SMTP_DATA["EMAIL"], password=SMTP_DATA["PASSWORD"])
            connection.sendmail(
                from_addr=SMTP_DATA["EMAIL"],
                to_addrs="moha.rezahosseini@gmail.com",
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{practice_url}".encode("utf-8")
            )
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    else:
        print(f"Price (${price_float}) is not below target (${BUY_PRICE}). No email sent.")