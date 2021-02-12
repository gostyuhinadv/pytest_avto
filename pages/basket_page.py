from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "guest CAN see product in basket"

    def guest_can_enter_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.TITLE_BASKET), "guest no enter to basket"

    def delete_item(self):
        button_delete = self.browser.find_element(*BasketPageLocators.DELETE_ITEM)
        button_delete.click()

    def check_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is not empty"

    def button_continue_shopping(self):
        button = self.browser.find_element(*BasketPageLocators.BUTTON_CONTINUE_SHOPPING)
        button.click()
