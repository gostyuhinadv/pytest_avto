import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
import time

@pytest.mark.need_review_custom_scenarios
def test_login_in_account_existing_account(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.enter_in_existing_account()
    page = MainPage(browser, browser.current_url)
    page.books_button_on_main_page()


