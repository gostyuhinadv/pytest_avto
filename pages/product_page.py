from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_product = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT_TO_BASKET)
        button_add_product.click()

    def success_message_about_add_product_in_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_SUCCESS_ADD_PRODUCT), "the product wasn't added to the basket"

    def choose_the_book(self):
        choose_book = self.browser.find_element(*ProductPageLocators.CHOOSE_BOOK)
        choose_book.click()

    def write_review_button(self):
        button_writw_review = self.browser.find_element(*ProductPageLocators.BUTTON_WRITE_REVIEW)
        button_writw_review.click()



