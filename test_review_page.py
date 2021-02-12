import pytest
from pages.review_page import ReviewPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import time

@pytest.mark.xfail
@pytest.mark.need_review_custom_scenarios
def test_write_review_by_guest(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/reviews/add/#addreview"
    page = ReviewPage(browser, link)
    page.open()
    page.write_review_by_guest()


class TestCreateNewUser:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(str(time.time()) + "@ya.ru", str(time.time()) + "h4bgh")
        page = MainPage(browser, browser.current_url)
        page.books_button_on_main_page()

    @pytest.mark.xfail
    @pytest.mark.need_review_custom_scenarios
    def test_write_review_by_user(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/reviews/add/#addreview"
        page = ReviewPage(browser, link)
        page.open()
        page.write_review_by_user()
