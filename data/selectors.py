
class Selectors:
    def __init__(self):
        self.email_textbox = ".mb-4:nth-child(3) .form-control"
        self.password_textbox = ".mb-4~ .mb-4 .form-control"
        self.login_button = ".btn-primary"
        self.create_board_nav = 'a.nav-link[href="/boards/create"]'
        self.session_textbox = "input[placeholder='Session Name']"
        self.owner = "div.card-body div.mb-4:nth-child(3) select"
        self.createboard_button = 'p.mb-4>a[href="/boards/create"]'
        self.title_textbox = "div.modal-body p.mb-0>input"
        self.create_button = "form button.btn-primary"
        self.plus_button = {
            "green": "div.my-2:nth-child(1)>div.m-0>button",
            "red": "div.my-2:nth-child(2)>div.m-0>button"
        }
        self.card = {
            "green": "div.my-2:nth-child(1) div.card",
            "red": "div.my-2:nth-child(2) div.card"
        }
        self.card_title = {
            "green": self.card["green"] + " h6.card-header",
            "red": self.card["red"] + " h6.card-header"
        }
        self.card_desc = {
            "green": self.card["green"] + " div.card-body > p",
            "red": self.card["red"] + " div.card-body > p"
        }
        self.card_button = "div.modal-footer button"
        self.desc_textbox = "p.mb-0 > textarea"
        self.like_button = {
            "green": self.card["green"] + " button[data-toggle='tooltip']",
            "red": self.card["red"] + " button[data-toggle='tooltip']"
        }
        self.like_icon = {
            "green": self.card["green"] + " svg.fa-thumbs-up",
            "red": self.card["red"] + " svg.fa-thumbs-up"
        }
        self.delete_card_button = {
            "green": self.card["green"] + " li:nth-child(2) button",
            "red": self.card["red"] + " li:nth-child(2) button"
        }
        self.created_popup = "div.swal-overlay"
        self.created_text = "div.swal-overlay div.swal-title"
        self.delete_card = "div.modal-content"
        self.delete_title = "div.modal-content div.h4"
        self.delete_desc = "div.modal-body > p"
        self.deletecard_button = "div.modal-footer > button"
        self.delete_success = "div.toast-success"
