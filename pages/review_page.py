from .base_page import BasePage
from .locators import ReviewPageLocators

class ReviewPage(BasePage):
    def button_review_is_worke(self):
        assert self.is_element_present(*ReviewPageLocators.REVIEW_STARS), "Button review not work"

    def write_review_by_guest(self):
        title = self.browser.find_element(*ReviewPageLocators.REVIEW_TITLE)
        title.send_keys("about Coders at Work")
        star = self.browser.find_element(*ReviewPageLocators.FIRST_STAR)
        star.click()
        body = self.browser.find_element(*ReviewPageLocators.BODY_REVIEW)
        body.send_keys("The worst book ever")
        name = self.browser.find_element(*ReviewPageLocators.NAME)
        name.send_keys("name")
        email = self.browser.find_element(*ReviewPageLocators.EMAIL)
        email.send_keys("fdfsssdfdf@ya.ru")
        button_save_review = self.browser.find_element(*ReviewPageLocators.SAVE_REVIEW)
        button_save_review.click()
        assert self.is_element_present(*ReviewPageLocators.CHECK_RESULT_OF_WRITING), "The review was'nt sent!"

    def write_review_by_user(self):
        title = self.browser.find_element(*ReviewPageLocators.REVIEW_TITLE)
        title.send_keys("about Coders at Work")
        star = self.browser.find_element(*ReviewPageLocators.FIRST_STAR)
        star.click()
        body = self.browser.find_element(*ReviewPageLocators.BODY_REVIEW)
        body.send_keys("The worst book ever")
        button_save_review = self.browser.find_element(*ReviewPageLocators.SAVE_REVIEW)
        button_save_review.click()
        assert self.is_element_present(*ReviewPageLocators.CHECK_RESULT_OF_WRITING), "The review was'nt sent!"