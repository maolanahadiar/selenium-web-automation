from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.settings import Config

class RadioButtonPage(BasePage):
    
    #LOCATORS
    ELEMENTS_MENU = (By.XPATH, "//h5[normalize-space()='Elements']")
    RADIO_BUTTON_MENU = (By.CSS_SELECTOR, "#item-2")
    RADIO_BUTTON_TITLE = (By.CSS_SELECTOR, ".text-center")
    YES_RADIO = (By.ID, "yesRadio")
    IMPRESSIVE_RADIO = (By.ID, "impressiveRadio")
    NO_RADIO = (By.ID, "noRadio")
    OUTPUT_TEXT = (By.CSS_SELECTOR, ".mt-3")
    
    def open_website(self):
        self.open_url(Config.BASE_URL)
        
    def open_radio_button_page(self):
        self.click(*self.ELEMENTS_MENU)
        self.click(*self.RADIO_BUTTON_MENU)
    
    def get_current_url_of_radio(self):
        return self.get_current_url()
        
    def get_page_title_of_radio(self):
        return self.get_text(*self.RADIO_BUTTON_TITLE)
    
    def click_radio_button_of_yes(self):
        self.click(*self.YES_RADIO)
    
    def click_radio_button_of_impressive(self):
        self.click(*self.IMPRESSIVE_RADIO)
    
    def is_radio_button_of_no_clickable(self):
        return self.is_element_clickable(*self.NO_RADIO)
    
    def get_actual_result(self):
        return self.get_text(*self.OUTPUT_TEXT)