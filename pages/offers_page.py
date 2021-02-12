from .base_page import BasePage
from .locators import OffersPageLocators

class OffersPage(BasePage):
    def guest_can_go_to_offers_page_from_main_page(self):
        assert self.is_element_present(*OffersPageLocators.OFFERS_TITLE), "guest didn't go to offer page"