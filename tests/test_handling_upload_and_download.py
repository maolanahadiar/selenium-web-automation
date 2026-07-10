from pages.upload_and_download_page import UploadDownloadPage
from config.settings import Config
from data.data_testing import UPLOAD_AND_DOWNLOAD

def test_handling_upload_and_download(browser):
    page = UploadDownloadPage(browser)
    
    #Navigate to the website
    page.open_upload_download_page()
    
    #Verify URL and title page 
    assert page.current_url_of_upload_download() == Config.UPLOAD_DOWNLOAD_URL
    assert page.get_page_title_of_upload_download() == UPLOAD_AND_DOWNLOAD["title_page"]
    
    #Download and upload file then verify the result
    page.download_image_file()
    page.upload_image_file("sampleFile.jpeg")
    
    assert page.get_actual_result() == UPLOAD_AND_DOWNLOAD["expected_result"]