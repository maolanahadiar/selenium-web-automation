from pages.buttons_page import ButtonsPage
from config.settings import Config
from data.data_testing import BUTTONS

def test_handling_buttons(browser):
    page = ButtonsPage(browser)
    
    #Navigate to the website
    page.open_website()
    page.open_buttons_page()
    
    #Verify URL and title page
    assert page.get_current_url() == Config.BUTTONS_URL
    assert page.get_page_title_of_button() == BUTTONS["title_page"]
    
    #Double click the button
    page.double_click_button()
    
    #Right click the button
    page.right_click_button()
    
    #Click dynamic element
    page.click_dynamic_element()
    
    #Verify the result
    assert page.get_actual_result_of_double_click() == BUTTONS["expected_result_of_double_click"]
    assert page.get_actual_result_of_right_click() == BUTTONS["expected_result_of_right_click"]
    assert page.get_actual_result_of_dynamic_element() == BUTTONS["expected_result_of_dynamic_element"]