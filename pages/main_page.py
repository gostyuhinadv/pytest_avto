from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def success_mesage_about_login_user(self):
        assert self.is_element_present(
            *MainPageLocators.SUCCESS_MESSAGE_ABOUT_USER_INNER), "the user did not login to his account"

    def go_to_product_page_from_mine_page(self):
        go_to_books_page = self.browser.find_element(*MainPageLocators.BUTTON_GO_TO_BOOKS_PAGE)
        go_to_books_page.click()

    def go_to_offers_page_from_mine_page(self):
        go_to_offers_page = self.browser.find_element(*MainPageLocators.BUTTON_GO_TO_OFFER_PAGE)
        go_to_offers_page.click()

    def books_button_on_main_page(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_GO_TO_BOOKS_PAGE), "user is not on the main page"

