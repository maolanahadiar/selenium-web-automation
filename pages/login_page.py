from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.settings import Config

class LoginPage(BasePage):

    # LOCATORS
    FIELD_USERNAME = (By.ID, "username")
    FIELD_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    RESPONSE_MESSAGE = (By.ID, "flash")

    def open(self):
        self.open_url(Config.LOGIN_URL)

    def input_login_form(self, username, password):
        self.type(*self.FIELD_USERNAME, text=username)
        self.type(*self.FIELD_PASSWORD, text=password)
        self.click(*self.BUTTON_LOGIN)

    def get_expected_message(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.visibility_of_element_located(self.RESPONSE_MESSAGE)
        )
        return element.text