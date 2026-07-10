from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Config

class CheckBoxPage(BasePage):
    
    #LOCATORS
    ELEMENTS_MENU = (By.XPATH, "//h5[normalize-space()='Elements']")
    CHECKBOX_MENU = (By.ID, "item-1")
    CHECKBOX_TITLE = (By.CSS_SELECTOR, ".text-center")
    SWITCHER_CLOSE_BUTTON = (By.CLASS_NAME, "rc-tree-switcher.rc-tree-switcher_close")
    SWITCHER_OPEN_BUTTON = (By.CSS_SELECTOR, ".rc-tree-switcher.rc-tree-switcher_open")
    DESKTOP_CHECKBOX = (By.XPATH, "//div/div[2]/span[3]")
    DOCUMENTS_CHECKBOX = (By.XPATH, "//div/div[3]/span[3]")
    DOWNLOADS_CHECKBOX = (By.XPATH, "//div/div[4]/span[3]")
    DESELECT_ALL_CHECKBOX = (By.CSS_SELECTOR, "div.rc-tree-list-holder-inner > div.rc-tree-treenode > span.rc-tree-checkbox")
    OUTPUT_TEXT = (By.ID, "result")
    
    def open_website(self):
        self.open_url(Config.BASE_URL)
    
    def open_checkbox_page(self):
        self.click(*self.ELEMENTS_MENU)
        self.click(*self.CHECKBOX_MENU)
    
    def current_url_of_checkbox(self):
        return self.get_current_url()
    
    def get_page_title_of_checkbox(self):
        return self.get_text(*self.CHECKBOX_TITLE)
    
    def open_checkbox_area(self):
        self.click(*self.SWITCHER_CLOSE_BUTTON)
        
    def click_desktop_checkbox(self):
        self.click(*self.DESKTOP_CHECKBOX)
        
    def click_documents_checkbox(self):
        self.click(*self.DOCUMENTS_CHECKBOX)
        
    def click_downloads_checkbox(self):
        self.click(*self.DOWNLOADS_CHECKBOX)
    
    def click_deselect_all_checkbox(self):
        self.click(*self.DESELECT_ALL_CHECKBOX)
        
    def get_actual_result(self):
        text = self.get_text(*self.OUTPUT_TEXT)
        text = text.replace("You have selected :", "")
        
        selected_items = set()

        for item in text.splitlines():
            item = item.strip()

            if item:
                selected_items.add(item)

        return selected_items
    
    def is_item_visible(self):
        return self.is_element_visible(*self.OUTPUT_TEXT)
    
    def close_checkbox_area(self):
        self.click(*self.SWITCHER_OPEN_BUTTON)