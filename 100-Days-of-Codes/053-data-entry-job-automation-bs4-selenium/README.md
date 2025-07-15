# Data Entry Job Automation
This project is part of the [100 Days of Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.

--- 

## Objective
Create an automated bot that uses **BeautifulSoup** and **Selenium** to perform a research data entry job based on client-defined criteria.
  - The bot scrapes house prices from **Zillow** website that match specific filters.
  - It then transfers the collected data into a web form, which automatically populates a Google Sheets spreadsheet.
  - This project simulates a real-world data entry workflow, automating a task that would typically be done manually.
  - The goal is to demonstrate practical web scraping skills while reducing the time and effort required for repetitive data entry tasks.

---

## Challenge 👺
1. **Specify the Search Criteria**
   - Let's assume that you have a client who wants you to compile a list of all the places that they can rent with these following criteria: 
     - Located in **San Francisco** 
     - Rent up to $3,000 per month
     - Must have at least one bedroom.
   - Because, San Francisco is notoriously expensive housing, and finding suitable housing can be very challenging.
     - On Zillow, you can filter listings based on these criteria:
       - Set the location to **San Francisco**, **California**
       - Select "**For Rent**" instead of "For Sale"
       - Switching the maximum price up to **$3,000**  
       - Add the extra requirement that it must have at least one bedroom.
   - While we could use the live version of Zillow to do this project for scraping,this comes with challenges:
     - Websites frequently get updated. So they might change the structure of HTML, and the names of CSS classes 
     - Pop-ups to the website or introduce captures  which causes issues for Selenium.
   - For this project, use a static clone of Zillow's website that already narrowed down the search criteria.
     - URL you should use with Selenium for this project: `https://appbrewery.github.io/Zillow-Clone`.
2. **Scrape Property Data Using BeautifulSoup**
   - Using the static Zillow clone URL and  your knowledge of **BeautifulSoup/Requests** to scrape through all data and extract the following details for each property:
     - **Price** — the monthly rental price
       - Create a list of prices for all the listings you scraped. 
       - Clean up the strings, by removing any "+" symbols and other information so that you are only left with a dollar price. 
       - The price should look like "$1,234" instead of "$1,234+ /mo"
     - **Address** — the full address of the listing
       - Create a list of addresses for all the listings you scraped.
       - Clean up the address data. Remove any newlines, pipe symbols (|), and unnecessary whitespace.
         - 👀 **HINT:** One way is to use Python's `.replace()` and `.strip()` methods to remove the newlines, whitespace and pipe symbols.
     - **Listing URL** — the link to the property details page
       - Create a list of links for all the listings you scraped.
   - 👀 **HINT:** Remember to provide your user agent and accepted languages via a **header**.
3. **Set up your own Google Form**
   - You need to create a new form in Google Forms.
     1. Go to https://docs.google.com/forms/ and create your own form:
     2. Add 3 questions to the form, make all questions "short-answer":
        - What's the address of property?
        - What's the price per month?
        - What's the link to the property?
     3. Click send and copy the link address of the form. You will need to use this in your program.
4. **Fill Out Data in the Google Form Using Selenium**
   - Once you've scraped all of that data using Beautiful Soup
   - You're going to be using Selenium to autofill in a Google form for each listing that you've scraped.
   - For each property:
     - Enter the address 
     - Enter price per month  
     - Enter link
   - You’ll submit the form once per property.
5. **Generate a Google Sheet from Form Responses**
   - Once all of that form's been compiled, then you'll have the option to turn it into a spreadsheet.
   - Open you Google form -> go to the **Responses tab** -> then click on **Link to Sheets** button -> to generate a Google sheet from the responses that have been submitted.
   - The spreadsheet will contain:
     - Address of the property
     - Price per month
     - Link to the property
6. **Deliver to Your Client**
   - once you've omp this research and automation: 
     - Share the Google sheet with your client 
     - They can filter down on each of the listings that match their criteria and decide which one they want to go and make a viewing.

---

## Requirements

- To run this script, you need:
    - **Python** >= 3.12
    - **request** >= 2.31
    - **BeautifulSoup** >= 4.12
    - **Selenium** >= 4.33
    - **Google Chrome**  browser installed.
    - [ChromeDriver](https://chromedriver.chromium.org/downloads) (Download the version matching your Chrome browser)
---

## Installation

### 1. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
# or
.venv\Scripts\activate     # For Windows
```

### 2. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/Reza-1988/DailyCoding.git
# Navigate to the project directory
cd DailyCoding/053-data-entry-job-automation-bs4-selenium
```

### 3. Install Requirements

```bash
pip install selenium, requests, beautifulsoup
```

### 4. Running the Bot

```bash
python data_entry_job.py
```
---