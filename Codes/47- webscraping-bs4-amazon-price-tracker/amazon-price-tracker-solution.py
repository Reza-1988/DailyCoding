import requests
from bs4 import BeautifulSoup
import smtplib
from Codes.local_settings import SMTP_DATA

# Step 1: Set up target price and product URL
BUY_PRICE = 100 # Set the price below which you would like to get a notification
PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Step 2: Fetch the webpage with headers
# Define headers to make the request look like it’s from a real browser
# User-Agent mimics a browser (e.g., Chrome on Windows)
# Accept-Language requests the page in a specific language (e.g., US English)
# Full headers would look something like this
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
#     "Dnt": "1",
#     "Priority": "u=1",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
# }

# A minimal header would look like this:
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
   "Accept-Language": "en-US,en;q=0.9"
 }
# Step 2: Fetch the webpage
response = requests.get(LIVE_URL, headers=header)

# Step 3: Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Debug the response
# Print the HTML to verify it’s the product page and not a CAPTCHA
# print(soup.prettify())  # Remove this line after debugging


# Step 5: Extract the product price from the HTML content
# Use BeautifulSoup's select_one() to locate the price element in the webpage's HTML.
# The price is contained in a <span> tag with class 'a-offscreen' that is nested inside
# an element with class 'a-price' (e.g., <div class="a-price"><span class="a-offscreen">$99.99</span></div>).
# The 'a-offscreen' class is used by Amazon to store the full price in a clean format, hidden from the visible page
# but accessible in the HTML for screen readers and scraping.
# The CSS selector '.a-price .a-offscreen' targets this specific <span> by looking for an element with class 'a-offscreen'
# that is a child of an element with class 'a-price'.
# The select_one() method returns the first matching element, which is sufficient since we expect only one main price.
# An alternative approach is to use soup.find(class_="a-offscreen"), but this is less precise as it doesn't ensure
# the element is nested under 'a-price' and could match other elements with 'a-offscreen' on the page.
try:
    price = soup.select_one(".a-price .a-offscreen").getText() # Alternative: price = soup.find(class_="a-offscreen").getText()
    price_float = float(price.strip().replace("$", "")) # Remove the dollar sign and convert to float for numerical comparison
except AttributeError:
    print("Price not found. Check HTML structure or CAPTCHA.")

# Step 6: Extract the product title
try:
    title = soup.find(id="productTitle").get_text().strip()
except AttributeError:
    print("Title not found. Check HTML structure or CAPTCHA.")



# Step 7: Check if price is below target and send email
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
                to_addrs="your_email",
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRACTICE_URL}".encode("utf-8")
            )
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
else:
    print(f"Price (${price_float}) is not below target (${BUY_PRICE}). No email sent.")