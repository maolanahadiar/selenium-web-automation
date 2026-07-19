from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Config

class DropdownPage(BasePage):
    
    #LOCATORS
    OLD_STYLE_DROPDOWN = (By.ID, "oldSelectMenu")
    SINGLE_SELECT_DROPDOWN = (By.ID, "selectOne")
    SINGLE_SELECT_OPTION = (By.XPATH, "//div[normalize-space()='Mr.']")
    MULTI_SELECT_DROPDOWN = (By.XPATH, "//div[normalize-space()='Select...']")
    BLUE_OPTION = (By.XPATH, "//div[@role='option' and text()='Blue']")
    BLACK_OPTION = (By.XPATH, "//div[@role='option' and text()='Black']")
    MULTI_SELECT_TEXT = (By.CSS_SELECTOR, ".css-1dyz3mf")

    def open_dropdown_page(self):
        self.open_url(Config.DROPDOWN_URL)
        
    def current_url_of_dropdown(self):
        return self.get_current_url()
    
    def select_html_dropdown(self, option):
        self.select_html_dropdown_by_text(*self.OLD_STYLE_DROPDOWN, text=option)
        
    def get_selected_value_of_html_dropdown(self):
        return self.get_html_dropdown_value(*self.OLD_STYLE_DROPDOWN)
    
    def select_react_single_dropdown(self):
        self.select_react_dropdown(self.SINGLE_SELECT_DROPDOWN, self.SINGLE_SELECT_OPTION)
        
    def get_selected_value_of_react_single_dropdown(self):
        return self.get_text(*self.SINGLE_SELECT_DROPDOWN)
    
    def select_react_multi_dropdown(self):
        self.select_react_dropdown(self.MULTI_SELECT_DROPDOWN, self.BLUE_OPTION)
        self.click(*self.BLACK_OPTION)
        self.click_outside_area()
        
    def get_selected_value_of_react_multi_dropdown(self):
        text = self.get_text(*self.MULTI_SELECT_TEXT)
        return ", ".join(text.splitlines())