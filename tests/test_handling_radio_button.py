from pages.radio_page import RadioButtonPage
from config.settings import Config
from testdata.page_titles import TITLES
from testdata.messages import MESSAGES

def test_handling_radio_button(browser):
    page = RadioButtonPage(browser)
    
    #Navigate to the website
    page.open_website()
    page.open_radio_button_page()
    
    #Verify URL and title page    
    assert page.get_current_url_of_radio() == Config.RADIO_URL
    assert page.get_page_title_of_radio() == TITLES["radio"]["page_title"]
    
    #Select radio button of "Yes" and verify the result
    page.click_radio_button_of_yes()
    assert page.get_actual_result() == MESSAGES["radio"]["expected_result_of_yes"]
    
    #Select radio button of "Impressive" and verify the result
    page.click_radio_button_of_impressive()
    assert page.get_actual_result() == MESSAGES["radio"]["expected_result_of_impressive"]
    
    #Verify radio button of "No" is not clickable
    assert not page.is_radio_button_of_no_clickable()