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




# this web driver which is going to be driving the Chrome browser and doing all of our automated tasks.
from selenium import webdriver

# Depending on whether if you're looking to find an element by class name or by ID, we need to use a class called, "By".
from selenium.webdriver.common.by import By


LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


"""to keep the browser open after our program finishes we have to configure our webdriver.
So to do that, we have to get hold of the Chrome options.We can get those via webdriver.chrome options
and then we have to add an experimental_option in Chrome called detach and set that option to true.
Now we pass that configuration over to our webdriver via parameter called options. And now when we run our Python program,
our Chrome browser doesn't close itself automatically anymore."""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# create a new driver from that new module. and then we can now instantiate any browser of our choice.
# So in our case we're going to be creating a Chrome browser to drive, but you can see that you can also have Firefox or Safari and a large number of other browsers.
driver = webdriver.Chrome(options=chrome_options) # notice that this is Chrome with a capital C.So we're initializing a new object here.


""" what this Chrome driver is,well here's the way to think about it.We've got our Selenium package, which contains code
for us to be able to interact with browsers. Now, it can interact with the Chrome browser
which is what we're choosing to do but it can also interact with a bunch of other ones like Safari or Firefox.
Now, how do we make sure that this package which can handle all three knows specifically how to work with the Chrome browser?
Well, we're going to need some sort of a bridge that bridges the Selenium code to work with the Chrome browser.
And this bridge is provided by the Chrome driver. So there'll be a different driver for Safari and there'll be a different driver for Firefox.
And just by switching up those drivers it'll tell Selenium how to work with the latest version of these browsers."""


driver.get(LIVE_URL) # use my driver to get it to open up a webpage.


"""if you want a particular class, or a particular ID, take a look at the Selenium Locator strategies. You can see here in the Selenium Docs,
there's many ways that we can find different elements on a page using Selenium. You can see that Selenium provides supportfor these eight traditional location strategies."""


# to figure out how to use Selenium to find and locate specific HTML elements on the webpage.ust between where we quit our driver and where we get hold of a particular page.

# to hold onto the dollar price element from the Amazon page. For the value, we'll grab the class name of the span from the Amazon page.
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# price_dollar and price_cents are actually an HTML element. So if we want to have the text that's inside those elements,
# we have to access the text content. And you can see here in the Selenium Docs, to get the text content,
# all we need to do is just write .text after we found the element. So we can add .text to the price_dollar and price_cent.
# So now we can actually get hold of the content that's inside those HTML elements.
print(f"the price is {price_dollar.text}.{price_cents.text}")


"""what's the difference between close and quit, you might wonder. Well, close actually just closes a single tab,
the active tab where you've opened up a particular page. Now quit is actually going to quit the entire browser.
I prefer actually just using quit() to shut down the entire browser. That way we can always start again from scratch and we'll have a fresh browser to work with."""

# we need to do is  driver.quit(), because otherwise, we're going to have a new instance of Chrome running every time I hit the Run button.
driver.quit()