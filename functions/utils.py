
from selenium import webdriver


class Utils:
    def __init__(self):
        self.browser = None

    def activate_browser(self):
        print("Activating browser...")
        self.browser = webdriver.Chrome()

    def open_url(self):
        self.browser.get("https://sprintboards.io/auth/login")
