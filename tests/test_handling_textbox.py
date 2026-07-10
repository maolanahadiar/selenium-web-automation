from pages.textbox_page import TextBoxPage
from config.settings import Config
from data.data_testing import TEXTBOX

def test_handling_textbox(browser):
    page = TextBoxPage(browser)
    
    #Navigate to the website
    page.open_website()
    page.open_textbox_page()
    
    #Verify URL and title page
    assert page.current_url_of_textbox() == Config.TEXTBOX_URL
    assert page.get_page_title_of_textbox() == TEXTBOX["title_page"]
    
    #Input textbox form and submit
    page.input_textbox_form(
        TEXTBOX["name"],
        TEXTBOX["email"],
        TEXTBOX["current_address"],
        TEXTBOX["permanent_address"]
    )
    page.click_submit_button()
    
    #Verify the result
    actual_result = page.get_actual_result()
    
    expected_result = {        
        "Name": TEXTBOX["name"],
        "Email": TEXTBOX["email"],
        "Current Address": TEXTBOX["current_address"],
        "Permananet Address": TEXTBOX["permanent_address"],
    }
    assert actual_result == expected_result