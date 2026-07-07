from pages.textbox_page import TextBoxPage
from config.settings import Config
from data.data_testing import TEXTBOX_DATA

def test_handling_textbox(browser):
    page = TextBoxPage(browser)
    
    #Navigate to the website
    page.open_website()
    page.open_textbox_page()
    
    #Verify URL and title page
    assert page.current_url_of_textbox() == Config.TEXTBOX_URL
    assert page.get_page_title_of_textbox() == TEXTBOX_DATA["title_page"]
    
    #Input textbox form and submit
    page.input_textbox_form(
        TEXTBOX_DATA["name"],
        TEXTBOX_DATA["email"],
        TEXTBOX_DATA["current_address"],
        TEXTBOX_DATA["permanent_address"]
    )
    page.click_submit_button()
    
    #Verify the result
    actual_result = page.get_actual_result()
    
    expected_result = {        
        "Name": TEXTBOX_DATA["name"],
        "Email": TEXTBOX_DATA["email"],
        "Current Address": TEXTBOX_DATA["current_address"],
        "Permananet Address": TEXTBOX_DATA["permanent_address"],
    }
    assert actual_result == expected_result