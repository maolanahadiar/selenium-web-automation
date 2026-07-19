from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Config

class TextBoxPage(BasePage):
    
    #LOCATORS
    ELEMENTS_MENU = (By.XPATH, "//h5[normalize-space()='Elements']")
    TEXTBOX_MENU = (By.ID, "item-0")
    TEXTBOX_TITLE = (By.CSS_SELECTOR, ".text-center")
    NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT =(By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON =(By.ID, "submit")
    OUTPUT_TEXT = (By.ID, "output")

    def open_textbox_page(self):
        self.open_url(Config.TEXTBOX_URL)
    
    def current_url_of_textbox(self):
        return self.get_current_url()
    
    def get_page_title_of_textbox(self):
        return self.get_text(*self.TEXTBOX_TITLE)
    
    def input_textbox_form(self, name, email, current_address, permanent_address):
        self.type(*self.NAME_INPUT, text=name)
        self.type(*self.EMAIL_INPUT, text=email)
        self.type(*self.CURRENT_ADDRESS_INPUT, text=current_address)
        self.type(*self.PERMANENT_ADDRESS_INPUT, text=permanent_address)
        self.click_outside_area()
    
    def click_submit_button(self):
        self.scroll_to_element(*self.SUBMIT_BUTTON)
        self.click(*self.SUBMIT_BUTTON)
        
    def get_actual_result(self):
        text = self.get_text(*self.OUTPUT_TEXT)
        result = {}

        for line in text.splitlines():
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
            
        return result