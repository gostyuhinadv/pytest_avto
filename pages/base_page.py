from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators, LoginPageLocators, BasketPageLocators




class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    #        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def go_to_login_page(self):
        button_login_page = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        button_login_page.click()

    def go_to_basket_page(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_GO_TO_BASKET)
        button_basket.click()
