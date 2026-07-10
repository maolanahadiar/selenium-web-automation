from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Config

class ButtonsPage(BasePage):
    
    #LOCATORS
    ELEMENTS_MENU = (By.XPATH, "//h5[normalize-space()='Elements']")
    BUTTONS_MENU = (By.ID, "item-4")
    BUTTONS_TITLE = (By.CSS_SELECTOR, ".text-center")
    DOUBLE_CLICK_BUTTON = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.ID, "rightClickBtn")
    DYNAMIC_ELEMENT_BUTTON = (By.XPATH, "//button[normalize-space()='Click Me']")
    DOUBLE_CLICK_MESSAGE = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.ID, "rightClickMessage")
    DYNAMIC_ELEMENT_MESSAGE = (By.ID, "dynamicClickMessage")
    
    def open_website(self):
        self.open_url(Config.BASE_URL)
        
    def open_buttons_page(self):
        self.click(*self.ELEMENTS_MENU)
        self.click(*self.BUTTONS_MENU)
        
    def get_current_url_of_button(self):
        return self.get_current_url()
        
    def get_page_title_of_button(self):
        return self.get_text(*self.BUTTONS_TITLE)
    
    def double_click_button(self):
        self.double_click(*self.DOUBLE_CLICK_BUTTON)
        
    def right_click_button(self):
        self.right_click(*self.RIGHT_CLICK_BUTTON)
    
    def click_dynamic_element(self):
        self.click(*self.DYNAMIC_ELEMENT_BUTTON)
        
    def get_actual_result_of_double_click(self):
        return self.get_text(*self.DOUBLE_CLICK_MESSAGE)
        
    def get_actual_result_of_right_click(self):
        return self.get_text(*self.RIGHT_CLICK_MESSAGE)
        
    def get_actual_result_of_dynamic_element(self):
        return self.get_text(*self.DYNAMIC_ELEMENT_MESSAGE)