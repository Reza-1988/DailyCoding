# Automated Job Application Bot
This project is part of the [100 Days of Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu.

--- 

## Objective
Create an automated bot that uses Selenium to apply for jobs on LinkedIn using the "Easy Apply" feature.
- The bot sends applications to all job listings that meet your defined criteria (not just one at a time).
- As an alternative, if you prefer not to send applications directly, the bot can "Save" the jobs and follow the companies instead.
- The goal is to reduce the repetitive effort of manual applications and explore automation in real-world workflows.

---

## 👺 Challenge
1. Set up a new email account
2. If you don't want to use your primary account for this project, feel free to set up a new LinkedIn account and Configure your Profile
   - Make sure you've signed up to LinkedIn.com and save your email and password somewhere for later use.
   - Do not enable 2-factor authentication/phone number verification while we are using Selenium.
   - Companies who look at your application will look through your LinkedIn profile to see if you have the skills and necessary work experience. If you are serious about applying for jobs make sure you update your LinkedIn Profile.
   - Upload your resume by going to:
        > Go to your LinkedIn profile -> Add a profile section -> Add media -> Upload your resume
3. Automatically Login
   1. Open a LinkedIn page -> Go to the Jobs tab 
       - Search for the job that you are interested in e.g. "Python developer". Add the "Easy Apply" filter and specify your desired location.
       - Copy the URL at the top of the address bar, it should contain all your requirements. e.g. https://www.linkedin.com/jobs/search/?currentJobId=4240382269&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true
   2. Use this URL in your script and what you know about Selenium, try to open the page by using the webdriver.
   3. When the LinkedIn job search page loads, a prompt may appear asking you how you'd like to sign in (e.g., "Sign in with email", "Continue with Google", etc.).
        - Figur out how to click Sign In button and navigate Sign In page.
   4. Figure out how to automatically log in to LinkedIn using Selenium with you LinkedIn account.
     - Locate and fill in the username(email or phone) and password fields.
     - Trigger the Sign In button to log into your LinkedIn account automatically.
4. Apply for a Job
   - Use Selenium to automatically apply to the first job that only requires you to enter your phone number. 