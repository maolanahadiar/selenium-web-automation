from pages.upload_and_download_page import UploadDownloadPage
from config.settings import Config
from testdata.page_titles import TITLES
from testdata.messages import MESSAGES

def test_handling_upload_and_download(browser):
    page = UploadDownloadPage(browser)
    
    #Navigate to the website
    page.open_upload_download_page()
    
    #Verify URL and title page 
    assert page.current_url_of_upload_download() == Config.UPLOAD_DOWNLOAD_URL
    assert page.get_page_title_of_upload_download() == TITLES["upload_and_download"]["page_title"]
    
    #Download and upload file then verify the result
    page.download_image_file()
    page.upload_image_file()
    
    assert page.get_actual_result() == MESSAGES["upload_and_download"]["expected_result"]