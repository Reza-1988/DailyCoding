# Cookie Clicker Bot with Selenium
This project is part of the [100 Days of Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.

---

## Objective
Create an **automated bot** uses `Selenium` and Python to automate gameplay in the Cookie Clicker game.
- The bot continuously clicks the big cookie to earn cookies (the game's currency)
- Intelligently purchases the most expensive affordable upgrade every 5 seconds to maximize cookie production efficiency. 
- The bot runs for 5 minutes and then displays the cookies-per-second rate.

---

## 👺 Challenge
1. Go to the game on web-site pages and familiarise yourself with how it works: [Cookie Clicker Game](https://orteil.dashnet.org/experiments/cookie/)
2. Create a bot using Selenium(a tool for automating web browsers) and Python to click on the cookie as fast as possible.
3. Every 5 seconds, check the right-hand pane to see which upgrades are affordable (like hiring grandmas or factories).
4. Purchase the most expensive one. You'll need to check how much money (cookies) you have against the price of each upgrade (e.g. both Grandma and Cursor are affordable as we have 105 cookies, but Grandma is the more expensive one, so we'll purchase that instead of the cursor).
   - **NOTE**: the most challenging part will be figuring out how to select the most expensive item every 5 seconds, since the upgrades become available only gradually over time.
5. Running bot for a total of 5 minutes.
6. After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second".

---


## Requirements

- To run this script, you need:
    - **Python** >= 3.12
    - **Selenium** >= 4.33
    - Google Chrome browser installed.
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
cd DailyCoding/048-cookie-clicker-bot-selenium
```

### 3. Install Requirements

```bash
pip install selenium
```

### 3. Running the Bot

```bash
python cookie_clicker_bot.py
```
---

- You should see the browser open, the cookie being clicked rapidly, and upgrades being purchased automatically.
After 5 minutes, the script will stop and display your cookies per second