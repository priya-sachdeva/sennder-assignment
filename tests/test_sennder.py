from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import chromedriver_binary

from functions.sennder import Sennder
sennder1 = Sennder()

from data.selectors import Selectors
selector1 = Selectors()

# Getting credentials from environment variables
import os
username=os.getenv("user")
password=os.getenv("password")

# Create browser instance
browser = webdriver.Chrome()

# Open the website
browser.get("https://sprintboards.io/auth/login")

# Login to the website
sennder1.login(browser,username,password)

#  Create board button and waiting for session textbox
sennder1.waitForElement(browser,selector1.createboard_button).click()
sennder1.waitForElement(browser,selector1. session_textbox)

# Check Browser Title and URL
assert browser.current_url == "https://sprintboards.io/boards/create"
assert "Create a Board" in browser.title

# Create Board
sennder1.createboard(browser)

# Add green card
sennder1.waitForElement(browser,selector1.green_button).click()
sennder1.waitForElement(browser,"body > div.fade.modal.show > div > div")
assert sennder1.getElementByCssSelector(browser, "#add-card-modal").text == "Add a Card"
sennder1.createcard(browser, 'Goal was achieved', 'Sprint was well planned')
sennder1.waitForElement(browser, selector1.green_card)
assert sennder1.getElementByCssSelector(browser,selector1.greencard_title).text == "Goal was achieved"
assert sennder1.getElementByCssSelector(browser,selector1.greencard_desc).text == "Sprint was well planned"

# Add red card
sennder1.getElementByCssSelector(browser,selector1.red_button).click()
sennder1.waitForElement(browser,"body > div.fade.modal.show > div > div")
assert sennder1.getElementByCssSelector(browser,"#add-card-modal").text == "Add a Card"
sennder1.createcard(browser, 'Goal was not achieved')
sennder1.waitForElement(browser,selector1.red_card)
assert sennder1.getElementByCssSelector(browser,selector1.redcard_title).text == "Goal was not achieved"
assert sennder1.getElementByCssSelector(browser,selector1.redcard_desc).text == "No description provided."

# Like green card
sennder1.like(browser)

# Delete red card
sennder1.delete(browser)

# Exit browser
browser.quit()
