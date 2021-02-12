from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def guest_can_get_login_page_from_basket_page(self):
        assert self.browser.find_element(
            *LoginPageLocators.BUTTON_GO_REGISTRATION), "failed to get to the registration form"

    def guest_can_get_login_page_from_main_page(self):
        assert self.browser.find_element(
            *LoginPageLocators.BUTTON_GO_REGISTRATION), "failed to get to the registration form"

    def enter_in_existing_account(self):
        email = self.browser.find_element(*LoginPageLocators.USER_EMAIL)
        email.send_keys("fdfsssdfdf@ya.ru")
        password = self.browser.find_element(*LoginPageLocators.USER_PASSWORD)
        password.send_keys("sdsdfd1288sese")
        button = self.browser.find_element(*LoginPageLocators.BUTTON_ENTER)
        button.click()

    def register_new_user(self, email, password):
        form_email = self.browser.find_element(*LoginPageLocators.NEW_USER_EMAIL)
        form_email.send_keys(email)
        form_password1 = self.browser.find_element(*LoginPageLocators.NEW_USER_PASS_1)
        form_password1.send_keys(password)
        form_password2 = self.browser.find_element(*LoginPageLocators.NEW_USER_PASS_2)
        form_password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.NEW_USER_BUTTON_REG)
        button.click()


