from pages.checkbox_page import CheckBoxPage
from config.settings import Config
from testdata.page_titles import TITLES
from testdata.messages import MESSAGES

def test_handling_checkbox(browser):
    page = CheckBoxPage(browser)
    
    #Navigate to the website
    page.open_website()
    page.open_checkbox_page()
    
    #Verify URL and title page    
    assert page.current_url_of_checkbox() == Config.CHECKBOX_URL
    assert page.get_page_title_of_checkbox() == TITLES["checkbox"]["page_title"]
    
    #Open checkbox area
    page.open_checkbox_area()
    
    #Select multi-checkbox and verify the result
    page.click_desktop_checkbox()
    page.click_documents_checkbox()
    page.click_downloads_checkbox()
    
    assert page.get_actual_result() == set(MESSAGES["checkbox"]["expected_result"])
    
    #Deselect all checkbox and verify the result
    page.click_deselect_all_checkbox()
    assert not page.is_item_visible()
    
    #Close checkbox area
    page.close_checkbox_area()