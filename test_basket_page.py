import pytest
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

@pytest.mark.xfail
@pytest.mark.need_review_custom_scenarios
def test_delete_item_from_basket_by_user(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.enter_in_existing_account()
    page = MainPage(browser, browser.current_url)
    page.go_to_product_page_from_mine_page()
    page = ProductPage(browser, browser.current_url)
    page.choose_the_book()
    page = ProductPage(browser, browser.current_url)
    page.add_product_to_basket()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.delete_item()
    page.check_that_basket_is_empty()

@pytest.mark.need_review_custom_scenarios
def test_button_continue_shopping_on_basket_page(browser):
    link = "http://selenium1py.pythonanywhere.com/basket/"
    page = BasketPage(browser, link)
    page.open()
    page.button_continue_shopping()
    page = MainPage(browser, browser.current_url)
    page.books_button_on_main_page()