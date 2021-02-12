from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.review_page import ReviewPage
import pytest
import time


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, browser.current_url)
    page.guest_can_get_login_page_from_basket_page()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_about_add_product_in_basket()

@pytest.mark.xfail
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.basket_should_be_empty()

@pytest.mark.need_review_custom_scenarios
def test_button_for_write_review_is_work(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.write_review_button()
    page = ReviewPage(browser, browser.current_url)
    page.button_review_is_worke()

class TestCreateNewUser:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(str(time.time()) + "@ya.ru", str(time.time()) + "h4bgh")
        page = MainPage(browser, browser.current_url)
        page.books_button_on_main_page()


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page = ProductPage(browser, browser.current_url)
        page.add_product_to_basket()
        page.success_message_about_add_product_in_basket()









