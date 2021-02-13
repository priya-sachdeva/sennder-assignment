import os

def test_login(sennder):
    sennder.open_url("https://sprintboards.io/auth/login")
    sennder.login(os.environ["USER_NAME"], os.environ["PWD"])


def test_create_board(sennder):
    board_title = "My first board"
    sennder.openCreateBoardPage()
    sennder.createboard(board_title)


def test_create_green_card(sennder):
    card_title = "Goal was achieved"
    card_desc = "Sprint was well planned"
    sennder.opencard("green")
    sennder.createcard("green", card_title, card_desc)


def test_create_red_card(sennder):
    card_title = "Goal was not achieved"
    sennder.opencard("red")
    sennder.createcard("red", card_title)


def test_like_green_card(sennder):
    sennder.like_card("green")


def test_delete_red_card(sennder):
    sennder.delete_card("red")
