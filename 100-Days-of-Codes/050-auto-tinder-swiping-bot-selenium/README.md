# Auto Tinder Swiping Bot
This project is part of the [100 Days of Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.
 
---

## Objective
Create an automated bot that uses Selenium and Python to interact with Tinder's web interface and perform automatic swiping actions.
- The bot logs in to [Tinder](https://tinder.com/) using Facebook credentials.
- It continuously swipes right on profiles to maximize match potential.
- When a match occurs, it detects and dismisses the popup to resume swiping.
- The bot respects Tinder's daily swipe limit and is intended for learning browser automation.

This project explores real-world use cases for Selenium by automating a popular web app in a fun and engaging way.
> ⚠️ Note: This project is for educational purposes only. Please use responsibly and ethically.

---

## 👺 Challenge
1. **Create a New Account**
    1. If you don't have a Tinder account, set one up now. Make sure you can sign in to your account using Facebook or Google.
       - If you don't want to use your own details, set up a new Facebook account and use an AI-generated image from https://www.thispersondoesnotexist.com/
         - HINT: You can hit refresh on thispersondoesnotexist to generate new random images.
    2. Manually go through the process of swiping on profiles and see which elements you'll need to target with your code.
   - NOTE: If you don't want to disappoint anyone, you can always complete the tutorial and hit "NOPE" on everyone. 
2. **Navigate to Login Page**
   - To avoid dual verification with a phone every time we log in. we'll need to use the Facebook/Google login. 
     - The Google login flow requires a lot more steps than Facebook login, so we'll go with Facebook login.
     - HINT 1: Make sure you've already manually signed-in and verified **your phone number** with Tinder as we can't automate the phone number verification.
     - HINT 2: If you are getting a `NoSuchElementException`, make sure you've added some delay between clicking on buttons so that the new element has enough time to load.
     - HINT 3: You might find it easier to right-click on the element and get the **XPath** to use with Selenium. e.g.
3. **Login with Facebook**
   1. The Facebook login page opens in a new window. For Selenium code to work on the new window, we have to switch to the window in front.
      - In Selenium, each window has an identification handle. We can get all the window handles with:  
        ```python
        driver.window_handles
        ```
      - The above line of code returns a list of all the window handles. The first window is at position `0`, e.g.:
        ```python
        base_window = driver.window_handles[0]
        ```
      - New windows that have popped out from the base window are further down in the sequence, e.g.:
        ```python
        fb_login_window = driver.window_handles[1]
        ```
      - We can switch our Selenium driver to target the new Facebook login window with:
        ```python
        driver.switch_to.window(fb_login_window)
        ```
      - You can print the `driver.title` to verify that it's the Facebook login window that is currently targeted:
        ```python
        print(driver.title)
        ```
      - The full code to switch to the new pop-up window is thus:
        ```python
        base_window = driver.window_handles[0]
        fb_login_window = driver.window_handles[1]
        driver.switch_to.window(fb_login_window)
        print(driver.title)
        ```
      - If successful, the printed title should be **"Facebook"** and not **"Tinder | Match. Chat. Date."**
   2. Using what you have learnt about Selenium, fill in the Facebook login form and submit it to log in.
   3. If successful, you should see the pop-up window disappear, and you're back on the Tinder page. e.g.
      - At this point, you should revert back to the base_window and verify by printing the title of the Selenium controlled window title.
      ```python
      driver.switch_to.window(base_window)
      print(driver.title)
      ```
      - If successful, it should print "Tinder | Match. Chat. Date."
4. **Step 4 - Dismiss all requests**