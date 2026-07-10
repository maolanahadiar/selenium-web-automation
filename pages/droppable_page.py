from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Config

class DragAndDropPage(BasePage):
    
    #LOCATORS
    DEMO_IFRAME = (By.CLASS_NAME, "demo-frame")
    DRAG_CARD = (By.ID, "draggable")
    DROP_CARD = (By.ID, "droppable")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#droppable > p")
    
    def open_droppable_page(self):
        self.open_url(Config.DROPPABLE_URL)
        
    def current_url_of_droppable(self):
        return self.get_current_url()
    
    def get_page_title_of_droppable(self):
        return self.get_title()
    
    def switch_to_iframe(self):
        self.switch_to_frame(*self.DEMO_IFRAME)
        
    def drag_and_drop_item(self):
        self.drag_and_drop(self.DRAG_CARD, self.DROP_CARD)
    
    def get_actual_result(self):
        return self.get_text(*self.SUCCESS_MESSAGE)