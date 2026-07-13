from pages.login_page import LoginPage
from config.settings import Config
from testdata.credentials import LOGIN
from testdata.page_titles import TITLES
from testdata.messages import MESSAGES

def test_login_success(browser):
    page = LoginPage(browser)

    #Navigate to the book store login page
    page.open_login_page()
    
    #Verify URL and title page
    assert page.current_url_of_login() == Config.LOGIN_URL
    assert page.get_page_title_of_login() == TITLES["login"]["page_title"]
    
    #Input login form using valid credential and verify the result
    page.input_login_form(
        LOGIN["valid"]["username"],
        LOGIN["valid"]["password"]
    )
    assert page.get_success_message() == MESSAGES["login"]["expected_result_of_success"]

def test_login_invalid(browser):
    page = LoginPage(browser)

    #Navigate to the website
    page.open_login_page()
    
    #Verify URL and title page
    assert page.current_url_of_login() == Config.LOGIN_URL
    assert page.get_page_title_of_login() == TITLES["login"]["page_title"]
    
    #Input login form using invalid credential and verify the result
    page.input_login_form(
        LOGIN["invalid"]["username"],
        LOGIN["invalid"]["password"]
    )
    assert page.get_error_message() == MESSAGES["login"]["expected_result_of_failed"]