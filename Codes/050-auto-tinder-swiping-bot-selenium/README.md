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
   - d
