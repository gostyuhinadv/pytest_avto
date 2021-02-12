from selenium.webdriver.common.by import By


class ProductPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, ".hidden-xs > span > a")
    ALERT_SUCCESS_ADD_PRODUCT = (By.XPATH, '//strong[contains(text(), "Coders at Work")]')
    CHOOSE_BOOK = (By.CSS_SELECTOR, '[title="Coders at Work"]')
    BUTTON_WRITE_REVIEW = (By.CSS_SELECTOR, '#write_review')

class LoginPageLocators:
    BUTTON_GO_REGISTRATION = (By.CSS_SELECTOR, '[name="registration_submit"]')
    USER_EMAIL = (By.CSS_SELECTOR, '[name="login-username"]')
    USER_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    BUTTON_ENTER = (By.CSS_SELECTOR, '[name="login_submit"]')
    NEW_USER_EMAIL = (By.CSS_SELECTOR, '[id="id_registration-email"]')
    NEW_USER_PASS_1 = (By.CSS_SELECTOR, '[id="id_registration-password1"]')
    NEW_USER_PASS_2 = (By.CSS_SELECTOR, '[id="id_registration-password2"]')
    NEW_USER_BUTTON_REG = (By.CSS_SELECTOR, '[name="registration_submit"]')

class BasketPageLocators:
    TITLE_BASKET = (By.CSS_SELECTOR, 'div.page-header h1')
    PRODUCT_IN_BASKET = (By.XPATH, '//a[contains(text(), "Coders at Work")]')
    DELETE_ITEM = (By.CSS_SELECTOR, '[data-behaviours="remove"]')
    BASKET_IS_EMPTY = (By.XPATH, '//p[contains(text(), " Your basket is empty.")]')
    BUTTON_CONTINUE_SHOPPING = (By.XPATH, '//a[contains(text(), "Continue shopping")]')

class MainPageLocators:
    SUCCESS_MESSAGE_ABOUT_USER_INNER = (By.CSS_SELECTOR, ".alertinner.wicon")
    BUTTON_GO_TO_BOOKS_PAGE = (By.XPATH, '//a[contains(text(), "Books")]')
    BUTTON_GO_TO_OFFER_PAGE = (By.XPATH, '//a[contains(text(), "Offers")]' or '//a[contains(text(), "Предложения")]')

class OffersPageLocators:
    OFFERS_TITLE = (By.XPATH, '//div//h1[contains(text(), "Offers")]' or '//div//h1[contains(text(), "Предложения")]')

class ReviewPageLocators:
    REVIEW_STARS = (By.CSS_SELECTOR, 'div.star-rating')
    REVIEW_TITLE = (By.CSS_SELECTOR, '#id_title')
    FIRST_STAR = (By.CSS_SELECTOR, '.icon-star')
    BODY_REVIEW = (By.CSS_SELECTOR, '#id_body')
    NAME = (By.CSS_SELECTOR, '#id_name')
    EMAIL = (By.CSS_SELECTOR, '#id_email')
    SAVE_REVIEW = (By.CSS_SELECTOR, '[data-loading-text="Saving..."]')
    CHECK_RESULT_OF_WRITING = (By.XPATH, '//h2[contains(text(), "The worst book ever")]')



