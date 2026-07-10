from pages.radio_page import RadioButtonPage
from config.settings import Config
from data.data_testing import RADIO

def test_handling_radio_button(browser):
    page = RadioButtonPage(browser)
    
    #Navigate to the website
    page.open_website()
    page.open_radio_button_page()
    
    #Verify URL and title page    
    assert page.get_current_url_of_radio() == Config.RADIO_URL
    assert page.get_page_title_of_radio() == RADIO["title_page"]
    
    #Select radio button of "Yes" and verify the result
    page.click_radio_button_of_yes()
    assert page.get_actual_result() == RADIO["expected_result_of_yes"]
    
    #Select radio button of "Impressive" and verify the result
    page.click_radio_button_of_impressive()
    assert page.get_actual_result() == RADIO["expected_result_of_impressive"]
    
    #Verify radio button of "No" is not clickable
    assert not page.is_radio_button_of_no_clickable()