from utilities import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import chromedriver_binary

# Getting credentials from environment variables
import os
username=os.getenv("user")
password=os.getenv("password")

# Create browser instance
browser = webdriver.Chrome()

# Open the website
browser.get("https://sprintboards.io/auth/login")

# Login to the website
login(browser,username,password)

#  Create board button and waiting for session textbox
waitForElement(browser,createboard_button).click()
waitForElement(browser,session_textbox)

# Check Browser Title and URL
assert browser.current_url == "https://sprintboards.io/boards/create"
assert "Create a Board" in browser.title

# Create Board
createboard(browser)

# Add green card
waitForElement(browser,green_button).click()
waitForElement(browser,"body > div.fade.modal.show > div > div")
assert getElementByCssSelector(browser, "#add-card-modal").text == "Add a Card"
createcard(browser, 'Goal was achieved', 'Sprint was well planned')
waitForElement(browser, green_card)
assert getElementByCssSelector(browser,greencard_title).text == "Goal was achieved"
assert getElementByCssSelector(browser,greencard_desc).text == "Sprint was well planned"

# Add red card
getElementByCssSelector(browser,red_button).click()
waitForElement(browser,"body > div.fade.modal.show > div > div")
assert getElementByCssSelector(browser,"#add-card-modal").text == "Add a Card"
createcard(browser, 'Goal was not achieved')
waitForElement(browser,red_card)
assert  getElementByCssSelector(browser,redcard_title).text == "Goal was not achieved"
assert  getElementByCssSelector(browser,redcard_desc).text == "No description provided."

# Like green card
like(browser)

# Delete red card
delete(browser)

# Exit browser
browser.quit()