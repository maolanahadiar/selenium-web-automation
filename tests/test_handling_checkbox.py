from pages.checkbox_page import CheckBoxPage
from config.settings import Config
from data.data_testing import CHECKBOX

def test_handling_checkbox(browser):
    page = CheckBoxPage(browser)
    
    #Navigate to the website
    page.open_website()
    page.open_checkbox_page()
    
    #Verify URL and title page    
    assert page.current_url_of_checkbox() == Config.CHECKBOX_URL
    assert page.get_page_title_of_checkbox() == CHECKBOX["title_page"]
    
    #Open checkbox area
    page.open_checkbox_area()
    
    #Select multi-checkbox and verify the result
    page.click_desktop_checkbox()
    page.click_documents_checkbox()
    page.click_downloads_checkbox()
    
    assert page.get_actual_result() == set(CHECKBOX["expected_result"])
    
    #Deselect all checkbox and verify the result
    page.click_deselect_all_checkbox()
    assert not page.is_item_visible()
    
    #Close checkbox area
    page.close_checkbox_area()