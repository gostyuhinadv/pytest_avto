from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.offers_page import OffersPage
import pytest

@pytest.mark.need_review_custom_scenarios
def test_go_to_login_page_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.guest_can_get_login_page_from_main_page()

@pytest.mark.need_review_custom_scenarios
def test_go_to_offers_page_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_offers_page_from_mine_page()
    page = OffersPage(browser, browser.current_url)
    page.guest_can_go_to_offers_page_from_main_page()


