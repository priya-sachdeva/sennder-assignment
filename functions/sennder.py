from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from data.selectors import Selectors
from webdriver_manager.chrome import ChromeDriverManager

selector = Selectors()


class Sennder:

    def __init__(self, wd=None):
        if not wd:
            self.wd = webdriver.Chrome(ChromeDriverManager().install())
            self.wd.maximize_window()

    def open_url(self, url):
        self.wd.get(url)

    def quit(self):
        self.wd.close()

    def login(self, username, pwd):
        self.waitforcss(selector.email_textbox)
        emailadd = self.wd.find_element_by_css_selector(selector.email_textbox)
        emailadd.send_keys(username)
        password = self.wd.find_element_by_css_selector(selector.password_textbox)
        password.send_keys(pwd)
        loginbutton = self.wd.find_element_by_css_selector(selector.login_button)
        loginbutton.click()
        self.waitforcss(selector.create_board_nav)

    def openCreateBoardPage(self):
        self.waitforcss(selector.create_board_nav).click()
        self.waitforcss(selector.session_textbox)

    def createboard(self, board_title):
        session_name = self.wd.find_element_by_css_selector(selector.session_textbox)
        session_name.send_keys(board_title)
        select = Select(self.wd.find_element_by_css_selector(selector.owner))
        select.select_by_visible_text('Sennder')
        self.waitforcss(selector.create_button).click()
        self.waitforcss(selector.created_popup)
        assert self.wd.find_element_by_css_selector(selector.created_text).text == "Created"
        assert self.wd.current_url == "https://sprintboards.io/boards/create"

    def opencard(self, color):
        self.waitforcss(selector.plus_button[color]).click()
        assert self.wd.find_element_by_css_selector("#add-card-modal").text == "Add a Card"

    def createcard(self, color, title, description=None):
        card_title = self.wd.find_element_by_css_selector(selector.title_textbox)
        card_title.send_keys(title)
        if description is not None:
            goaldesc = self.wd.find_element_by_css_selector(selector.desc_textbox)
            goaldesc.send_keys(description)
        addcardbutton = self.wd.find_element_by_css_selector(selector.card_button)
        addcardbutton.click()
        self.waitforcss(selector.card[color])
        assert self.wd.find_element_by_css_selector(selector.card_title[color]).text == title
        if description:
            assert self.wd.find_element_by_css_selector(selector.card_desc[color]).text == description

    def like_card(self, color):
        likebutton = self.wd.find_element_by_css_selector(selector.like_button[color])
        assert likebutton.text == "0"
        likebutton.click()
        self.waitforcss(selector.like_icon[color])
        assert likebutton.text == "1"

    def delete_card(self, color):
        total_cards = len(self.wd.find_elements_by_css_selector(selector.card[color]))
        self.wd.find_element_by_css_selector(selector.delete_card_button[color]).click()
        self.waitforcss(selector.delete_card)
        deletetitle = self.wd.find_element_by_css_selector(selector.delete_title)
        assert deletetitle.text == "Delete Card"
        deletedesc = self.wd.find_element_by_css_selector(selector.delete_desc)
        assert deletedesc.text == "Are you sure you want to continue?"
        deletebutton = self.wd.find_element_by_css_selector(selector.deletecard_button)
        deletebutton.click()
        self.waitforcss(selector.delete_success)
        assert len(self.wd.find_elements_by_css_selector(selector.card[color])) == total_cards - 1

    def waitforcss(self, cssSelector):
        return WebDriverWait(self.wd, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))
