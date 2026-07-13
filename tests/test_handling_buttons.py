from pages.buttons_page import ButtonsPage
from config.settings import Config
from testdata.page_titles import TITLES
from testdata.messages import MESSAGES

def test_handling_buttons(browser):
    page = ButtonsPage(browser)
    
    #Navigate to the website
    page.open_website()
    page.open_buttons_page()
    
    #Verify URL and title page
    assert page.get_current_url() == Config.BUTTONS_URL
    assert page.get_page_title_of_button() == TITLES["buttons"]["page_title"]
    
    #Double click the button
    page.double_click_button()
    
    #Right click the button
    page.right_click_button()
    
    #Click dynamic element
    page.click_dynamic_element()
    
    #Verify the result
    assert page.get_actual_result_of_double_click() == MESSAGES["buttons"]["expected_result_of_double_click"]
    assert page.get_actual_result_of_right_click() == MESSAGES["buttons"]["expected_result_of_right_click"]
    assert page.get_actual_result_of_dynamic_element() == MESSAGES["buttons"]["expected_result_of_dynamic_element"]