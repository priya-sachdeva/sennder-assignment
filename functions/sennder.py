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

    def waitForElement(self,browser, cssSelector):
        return WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))

    def getElementByCssSelector(self,browser, cssSelector):
        return browser.find_element_by_css_selector(cssSelector)

    def getElementsByCssSelector(self,browser, cssSelector):
        return browser.find_elements_by_css_selector(cssSelector)

    def login(self,browser, username, pwd):
        self.waitForElement(browser, selector.email_textbox)
        emailadd = self.getElementByCssSelector(browser, selector.email_textbox)
        emailadd.send_keys(username)
        password = self.getElementByCssSelector(browser, selector.password_textbox)
        password.send_keys(pwd)
        loginbutton = self.getElementByCssSelector(browser, selector.login_button)
        loginbutton.click()

    def createboard(self,browser):
        session_name = self.getElementByCssSelector(browser, selector.session_textbox)
        session_name.send_keys('My first board')
        select = Select(self.getElementByCssSelector(browser, selector.owner))
        select.select_by_visible_text('Sennder')
        self.waitForElement(browser, selector.create_button).click()
        self.waitForElement(browser, selector.created_popup)
        assert self.getElementByCssSelector(browser, selector.created_text).text == "Created"
        assert browser.current_url == "https://sprintboards.io/boards/create"

    def createcard(self,browser, title, description=None):
        card_title = self.getElementByCssSelector(browser, selector.title_textbox)
        card_title.send_keys(title)
        if description is not None:
            goaldesc = self.getElementByCssSelector(browser, selector.desc_textbox)
            goaldesc.send_keys(description)
        addcardbutton = self.getElementByCssSelector(browser, selector.card_button)
        addcardbutton.click()

    def like(self,browser):
        likeButton = self.getElementByCssSelector(browser, selector.like_button)
        assert likeButton.text == "0"
        likeButton.click()
        time.sleep(3)
        assert likeButton.text == "1"

    def delete(self,browser):
        self.getElementByCssSelector(browser, selector.delete_button).click()
        self.waitForElement(browser, selector.delete_card)
        deletetitle = self.getElementByCssSelector(browser, selector.delete_title)
        assert deletetitle.text == "Delete Card"
        deletedesc = self.getElementByCssSelector(browser, selector.delete_desc)
        assert deletedesc.text == "Are you sure you want to continue?"
        deletebutton = self.getElementByCssSelector(browser, selector.deletecard_button)
        deletebutton.click()
        time.sleep(5)
        assert len(self.getElementsByCssSelector(browser, selector.card_number)) == 1


