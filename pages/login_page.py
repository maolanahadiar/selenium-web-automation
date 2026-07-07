from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Config

class LoginPage(BasePage):

    # LOCATORS
    LOGIN_TITLE = (By.CSS_SELECTOR, ".text-center")
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    USERNAME_LABEL = (By.ID, "userName-value")
    ERROR_MESSAGE = (By.ID, "name")

    def open_login_page(self):
        self.open_url(Config.LOGIN_URL)
    
    def current_url_of_login(self):
        return self.get_current_url()
    
    def get_page_title_of_login(self):
        return self.get_text(*self.LOGIN_TITLE)

    def input_login_form(self, username, password):
        self.type(*self.USERNAME_INPUT, text=username)
        self.type(*self.PASSWORD_INPUT, text=password)
        self.click(*self.LOGIN_BUTTON)

    def get_expected_message(self):
        return self.get_text(*self.USERNAME_LABEL)
    
    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)