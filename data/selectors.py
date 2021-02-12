# email_textbox = ".mb-4:nth-child(3) .form-control"
# password_textbox = ".mb-4~ .mb-4 .form-control"
# login_button = ".btn-primary"
# create_board = "#navbar > ul > li:nth-child(1) > a"
# session_textbox = "input[placeholder='Session Name']"
# owner = "form>div.card:nth-child(1) div.mb-4:nth-child(3) select"
# createboard_button = "div.w-100.bg-dark.p-4.p-lg-5:nth-child(1) div.container.pb-lg-5 div.row div.col.col-12.col-xl-6.text-center.text-xl-left:nth-child(1) p.d-flex.justify-content-center.justify-content-xl-start.align-items-center.mb-4 > a.btn.btn-lg.btn-primary.font-weight-light.mr-5.px-4.pt-2:nth-child(1)"
# title_textbox = "body > div.fade.modal.show > div > div > div.modal-body > form > div:nth-child(1) > p.mb-0 > input"
# create_button = "#wrapper-inner > div > form > div.w-100.text-center > button"
# green_button = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > button"
# card_button = "body > div.fade.modal.show > div > div > div.modal-footer.justify-content-start > form > p > button"
# green_card = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > h6"
# greencard_title = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > h6"
# greencard_desc = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > div > p"
# desc_textbox = "body > div.fade.modal.show > div > div > div.modal-body > form > div:nth-child(2) > p.mb-0 > textarea"
# red_button = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(2) > div > button"
# red_card = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(2) > div > div > div > h6"
# redcard_title = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(2) > div > div > div > h6"
# redcard_desc = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(2) > div > div > div > div > p"
# like_button = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > div > div:nth-child(3) > ul > li.ml-3 > button"
# delete_button =  "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(2) > div > div > div > div > div:nth-child(3) > ul > li:nth-child(2) > button"
# created_popup = "body > div.swal-overlay.swal-overlay--show-modal > div"
# created_text = "body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-title"
# delete_card = "body > div.fade.modal.show > div > div"
# delete_title = "body > div.fade.modal.show > div > div > div.modal-header > div"
# delete_desc = "body > div.fade.modal.show > div > div > div.modal-body > p"
# deletecard_button = "body > div.fade.modal.show > div > div > div.modal-footer.justify-content-start > button"
# card_number = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > h6"


class Selectors:
    def __init__(self):
        self.email_textbox = ".mb-4:nth-child(3) .form-control"
        self.password_textbox = ".mb-4~ .mb-4 .form-control"
        self.login_button = ".btn-primary"
        self.create_board = 'a.nav-link[href="/boards/create"]'
        self.session_textbox = "input[placeholder='Session Name']"
        self.owner = "div.card-body div.mb-4:nth-child(3) select"
        self.createboard_button = 'p.mb-4>a[href="/boards/create"]'
        self.title_textbox = "body > div.fade.modal.show > div > div > div.modal-body > form > div:nth-child(1) > p.mb-0 > input"
        self.create_button = "form button.btn-primary"
        self.green_button = 'div.my-2>div.m-0>button[data-column="8040bb2e-0571-410c-9360-56fce537d273"]'
        self.card_button = "body > div.fade.modal.show > div > div > div.modal-footer.justify-content-start > form > p > button"
        self.green_card = 'div[data-card="035be8fe-a633-4bd4-8615-8b630d7d0223"]'
        self.greencard_title = 'div[data-card="035be8fe-a633-4bd4-8615-8b630d7d0223"] h6.card-header'
        self.greencard_desc = 'div[data-card="035be8fe-a633-4bd4-8615-8b630d7d0223"] div.card-body > p'
        self.desc_textbox = "p.mb-0 > textarea"
        self.red_button = 'div.my-2>div.m-0>button[data-column="b6b65776-6696-465f-8f37-74b56603efb5"]'
        self.red_card = 'div[data-card="85b6c6f5-6aa3-42d0-b03d-85d73f7aac22"]'
        self.redcard_title = 'div[data-card="85b6c6f5-6aa3-42d0-b03d-85d73f7aac22"] h6.card-header'
        self.redcard_desc = 'div[data-card="85b6c6f5-6aa3-42d0-b03d-85d73f7aac22"] div.card-body > p'
        self.like_button = 'button.pointer-events[data-card="035be8fe-a633-4bd4-8615-8b630d7d0223"]'
        self.delete_button = 'li:nth-child(2) > button[data-card="85b6c6f5-6aa3-42d0-b03d-85d73f7aac22"]'
        self.created_popup = "div.swal-overlay.swal-overlay--show-modal > div"
        self.created_text = "div.swal-overlay.swal-overlay--show-modal > div > div.swal-title"
        self.delete_card = "div.fade.modal.show > div > div"
        self.delete_title = "div.fade.modal.show > div > div > div.modal-header > div"
        self.delete_desc = "div.fade.modal.show > div > div > div.modal-body > p"
        self.deletecard_button = "div.fade.modal.show > div > div > div.modal-footer.justify-content-start > button"
        self.card_number = "#wrapper > div > div.w-100.position-relative.d-flex.flex-column > div.d-flex.flex-column.flex-lg-row.flex-fill.px-1 > div:nth-child(1) > div > div > div > h6"

