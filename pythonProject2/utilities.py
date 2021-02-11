from data.selectors import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def waitForElement(browser, cssSelector):
    return WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))

def getElementByCssSelector(browser, cssSelector):
    return browser.find_element_by_css_selector(cssSelector)

def getElementsByCssSelector(browser, cssSelector):
    return browser.find_elements_by_css_selector(cssSelector)

def login(browser, username, pwd):
    waitForElement(browser, email_textbox)
    emailadd = getElementByCssSelector(browser,email_textbox)
    emailadd.send_keys(username)
    password = getElementByCssSelector(browser,password_textbox)
    password.send_keys(pwd)
    loginbutton = getElementByCssSelector(browser,login_button)
    loginbutton.click()


def createboard(browser):
    session_name = getElementByCssSelector(browser, session_textbox)
    session_name.send_keys('My first board')
    select = Select(getElementByCssSelector(browser, owner))
    select.select_by_visible_text('Sennder')
    waitForElement(browser,create_button).click()
    waitForElement(browser, created_popup)
    assert getElementByCssSelector(browser, created_text).text == "Created"
    assert browser.current_url == "https://sprintboards.io/boards/create"


def createcard(browser, title, description = None):
    card_title = getElementByCssSelector(browser, title_textbox)
    card_title.send_keys(title)
    if description is not None:
        goaldesc = getElementByCssSelector(browser, desc_textbox)
        goaldesc.send_keys(description)
    addcardbutton = getElementByCssSelector(browser, card_button)
    addcardbutton.click()

def like(browser):
    likeButton = getElementByCssSelector(browser, like_button)
    assert likeButton.text == "0"
    likeButton.click()
    time.sleep(3)
    assert likeButton.text == "1"

def delete(browser):
    getElementByCssSelector(browser,delete_button).click()
    waitForElement(browser,delete_card)
    deletetitle = getElementByCssSelector(browser, delete_title)
    assert deletetitle.text == "Delete Card"
    deletedesc = getElementByCssSelector(browser, delete_desc)
    assert deletedesc.text == "Are you sure you want to continue?"
    deletebutton = getElementByCssSelector(browser, deletecard_button)
    deletebutton.click()
    time.sleep(5)
    assert  len(getElementsByCssSelector(browser, card_number)) == 1

