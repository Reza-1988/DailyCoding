# Automated Job Application Bot
This project is part of the [100 Days of Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.

--- 

## Objective
Create an automated bot that uses Selenium to apply for jobs on LinkedIn using the "Easy Apply" feature.
- The bot sends applications to all job listings that meet your defined criteria (not just one at a time).
- As an alternative, if you prefer not to send applications directly, the bot can "Save" the jobs and follow the companies instead.
- The goal is to reduce the repetitive effort of manual applications and explore automation in real-world workflows.

---

## Challenge 👺
1. **Create a New Account**
   - Set up a new email account
   - If you don't want to use your primary account for this project, feel free to set up a new LinkedIn account and Configure your Profile
   - Make sure you've signed up to LinkedIn.com and save your email and password somewhere for later use.
   - Do not enable 2-factor authentication/phone number verification while we are using Selenium.
   - Companies who look at your application will look through your LinkedIn profile to see if you have the skills and necessary work experience. If you are serious about applying for jobs make sure you update your LinkedIn Profile.
   - Upload your resume by going to:
     - Go to your LinkedIn profile -> Add a profile section -> Add media -> Upload your resume
2. **Automatically Login**
   1. Open a LinkedIn page -> Go to the Jobs tab 
       - Search for the job that you are interested in e.g. "Python developer". Add the "Easy Apply" filter and specify your desired location.
       - Copy the URL at the top of the address bar, it should contain all your requirements. e.g. https://www.linkedin.com/jobs/search/?currentJobId=4240382269&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true
   2. Use this URL in your script and what you know about Selenium, try to open the page by using the webdriver.
   3. When the LinkedIn job search page loads, a prompt may appear asking you how you'd like to sign in (e.g., "Sign in with email", "Continue with Google", etc.).
        - Figur out how to click Sign In button and navigate Sign In page.
   4. Figure out how to automatically log in to LinkedIn using Selenium with you LinkedIn account.
     - Locate and fill in the username(email or phone) and password fields.
     - Trigger the Sign-In button to log into your LinkedIn account automatically.
3. **Apply for a Job**
   - Use Selenium to automatically apply to the first job that only requires you to enter your phone number. 
4. **Apply for all the jobs**
    - Figure out how to get your Selenium bot to apply to all the jobs on the page. Clicking on each job on the left hand side in-turn and applying to each one automatically. 
    - The jobs need to have these above conditions:
      - We're only going to apply to the standard, 1-step applications
      - We're going to ignore the applications that require a note
      - We're going to ignore the complex, multistep applications
    - Figur our how to ignore the complex application by checking the `data-control-name` attribute for Submit Button.
   - 👀 **HINT:** Selenium has a custom exception that gets raised when an element cannot be found it's called `NoSuchElementException`, You'll need to import it to use it:
   ```python
     from selenium.common.exceptions import NoSuchElementException
   ```
5. if You don't want to send an application right now  
   - You can adapt the project to save (all) the job(s) and follow the company that posted the listing(s) instead.
   - Instead of going with Easy Apply button, going with Save button.

---

## Requirements

- To run this script, you need:
    - **Python** >= 3.12
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
cd DailyCoding/049-automated_job_application_bot.py
```

### 3. Install Requirements

```bash
pip install selenium
```

### 4. Running the Bot

```bash
python automated_job_application_bot.py
```
---

You should see the script will launch a browser, automatically sign in to LinkedIn, and begin applying to jobs that match your specified criteria.