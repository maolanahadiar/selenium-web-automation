from pages.dropdown_page import DropdownPage
from config.settings import Config
from testdata.messages import MESSAGES
from testdata.sample_data import DROPDOWN

def test_handling_dropdown(browser):
    page = DropdownPage(browser)
    
    #Navigate to the website
    page.open_dropdown_page()
    assert page.get_current_url() == Config.DROPDOWN_URL
    
    #Select old dropdown then verify
    page.select_html_dropdown(DROPDOWN["option"])
    assert page.get_selected_value_of_html_dropdown() == MESSAGES["dropdown"]["expected_result_old_dropdown"]
    
    #Select custom single dropdown then verify
    page.select_react_single_dropdown()
    assert page.get_selected_value_of_react_single_dropdown() == MESSAGES["dropdown"]["expected_result_custom_single_dropdown"]
    
    #Select custom multi dropdown then verify
    page.select_react_multi_dropdown()
    assert page.get_selected_value_of_react_multi_dropdown() == MESSAGES["dropdown"]["expected_result_custom_multi_dropdown"]