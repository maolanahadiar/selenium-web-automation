from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.settings import Config

class LoginPage(BasePage):

    # LOCATORS
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    EXPECTED_MSG = (By.ID, "flash")

    def open(self):
        self.open_url(Config.LOGIN_URL)

    def login(self, username, password):
        self.type(*self.USERNAME, text=username)
        self.type(*self.PASSWORD, text=password)
        self.click(*self.LOGIN_BTN)

    def get_expected_message(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.visibility_of_element_located(self.EXPECTED_MSG)
        )
        return element.text