from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.settings import Config

class UploadDownloadPage(BasePage):
    
    #LOCATORS
    UPLOAD_DOWNLOAD_TITLE = (By.CSS_SELECTOR, ".text-center")
    UPLOAD_BUTTON = (By.ID, "uploadFile")
    FILEPATH_TEXT = (By.ID, "uploadedFilePath")
    DOWNLOAD_BUTTON = (By.ID, "downloadButton")
    
    def open_upload_download_page(self):
        self.open_url(Config.UPLOAD_DOWNLOAD_URL)
        
    def current_url_of_upload_download(self):
        return self.get_current_url()
    
    def get_page_title_of_upload_download(self):
        return self.get_text(*self.UPLOAD_DOWNLOAD_TITLE)
    
    def download_image_file(self):
        self.click(*self.DOWNLOAD_BUTTON)
        
    def upload_image_file(self, file_name):
        self.upload_file(*self.UPLOAD_BUTTON, file_name)
        
    def get_actual_result(self):
        return self.get_text(*self.FILEPATH_TEXT)