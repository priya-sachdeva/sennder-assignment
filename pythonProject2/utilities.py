from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


email_textbox = ".mb-4:nth-child(3) .form-control"
password_textbox = ".mb-4~ .mb-4 .form-control"
login_button = ".btn-primary"
create_board = "#navbar > ul > li:nth-child(1) > a"
session_textbox = "#wrapper-inner > div > form > div.card.border-0.shadow-sm.mt-4.mt-lg-0.mb-4.px-3.py-1 > div > div:nth-child(2) > input"
owner = "#wrapper-inner > div > form > div.card.border-0.shadow-sm.mt-4.mt-lg-0.mb-4.px-3.py-1 > div > div:nth-child(3) > select"
createboard_button = "div.w-100.bg-dark.p-4.p-lg-5:nth-child(1) div.container.pb-lg-5 div.row div.col.col-12.col-xl-6.text-center.text-xl-left:nth-child(1) p.d-flex.justify-content-center.justify-content-xl-start.align-items-center.mb-4 > a.btn.btn-lg.btn-primary.font-weight-light.mr-5.px-4.pt-2:nth-child(1)"
title_textbox = "body > div.fade.modal.show > div > div > div.modal-body > form > div:nth-child(1) > p.mb-0 > input"
create_button = "#wrapper-inner > div > form > div.w-100.text-center > button"
green_button = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > button"
card_button = "body > div.fade.modal.show > div > div > div.modal-footer.justify-content-start > form > p > button"
green_card = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > h6"
greencard_title = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > h6"
greencard_desc = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > div > p"
red_button = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(2) > div > button"
red_card = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(2) > div > div > div > h6"
redcard_title = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(2) > div > div > div > h6"
redcard_desc = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(2) > div > div > div > div > p"
like_button = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > div > div:nth-child(3) > ul > li.ml-3 > button"
delete_button =  "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(2) > div > div > div > div > div:nth-child(3) > ul > li:nth-child(2) > button"
created_popup = "body > div.swal-overlay.swal-overlay--show-modal > div"
created_text = "body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-title"
delete_card = "body > div.fade.modal.show > div > div"
delete_title = "body > div.fade.modal.show > div > div > div.modal-header > div"
delete_desc = "body > div.fade.modal.show > div > div > div.modal-body > p"
deletecard_button = "body > div.fade.modal.show > div > div > div.modal-footer.justify-content-start > button"
card_number = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > h6"

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
        goaldesc = getElementByCssSelector(browser, "body > div.fade.modal.show > div > div > div.modal-body > form > div:nth-child(2) > p.mb-0 > textarea")
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

