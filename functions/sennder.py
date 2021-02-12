from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from data.selectors import Selectors

selector = Selectors()

class Sennder:

    def __init__(self, wd=None):
        if not wd:
            self.wd = webdriver.Chrome()

    def open_url(self, url):
        self.wd.get(url)

    def quit(self):
        self.wd.close()

    def waitForElement(browser, cssSelector):
        return WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))

    def getElementByCssSelector(browser, cssSelector):
        return browser.find_element_by_css_selector(cssSelector)

    def getElementsByCssSelector(browser, cssSelector):
        return browser.find_elements_by_css_selector(cssSelector)

    def login(browser, username, pwd):
        waitForElement(browser, selector.email_textbox)
        emailadd = getElementByCssSelector(browser, selector.email_textbox)
        emailadd.send_keys(username)
        password = getElementByCssSelector(browser, selector.password_textbox)
        password.send_keys(pwd)
        loginbutton = getElementByCssSelector(browser, selector.login_button)
        loginbutton.click()

    def createboard(browser):
        session_name = getElementByCssSelector(browser, selector.session_textbox)
        session_name.send_keys('My first board')
        select = Select(getElementByCssSelector(browser, selector.owner))
        select.select_by_visible_text('Sennder')
        waitForElement(browser, selector.create_button).click()
        waitForElement(browser, selector.created_popup)
        assert getElementByCssSelector(browser, selector.created_text).text == "Created"
        assert browser.current_url == "https://sprintboards.io/boards/create"

    def createcard(browser, title, description=None):
        card_title = getElementByCssSelector(browser, selector.title_textbox)
        card_title.send_keys(title)
        if description is not None:
            goaldesc = getElementByCssSelector(browser, selector.desc_textbox)
            goaldesc.send_keys(description)
        addcardbutton = getElementByCssSelector(browser, selector.card_button)
        addcardbutton.click()

    def like(browser):
        likeButton = getElementByCssSelector(browser, selector.like_button)
        assert likeButton.text == "0"
        likeButton.click()
        time.sleep(3)
        assert likeButton.text == "1"

    def delete(browser):
        getElementByCssSelector(browser, selector.delete_button).click()
        waitForElement(browser, selector.delete_card)
        deletetitle = getElementByCssSelector(browser, selector.delete_title)
        assert deletetitle.text == "Delete Card"
        deletedesc = getElementByCssSelector(browser, selector.delete_desc)
        assert deletedesc.text == "Are you sure you want to continue?"
        deletebutton = getElementByCssSelector(browser, selector.deletecard_button)
        deletebutton.click()
        time.sleep(5)
        assert len(getElementsByCssSelector(browser, selector.card_number)) == 1


