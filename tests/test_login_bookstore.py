from pages.login_page import LoginPage
from data.data_testing import VALID_LOGIN, INVALID_LOGIN
from config.settings import Config

def test_login_success(browser):
    page = LoginPage(browser)

    #Navigate to the book store login page
    page.open_login_page()
    
    #Verify URL and title page
    assert page.current_url_of_login() == Config.LOGIN_URL
    assert page.get_page_title_of_login() == VALID_LOGIN["title_page"]
    
    #Input login form using valid credential and verify the result
    page.input_login_form(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )
    assert page.get_expected_message() == VALID_LOGIN["expected_result"]

def test_login_invalid(browser):
    page = LoginPage(browser)

    #Navigate to the website
    page.open_login_page()
    
    #Verify URL and title page
    assert page.current_url_of_login() == Config.LOGIN_URL
    assert page.get_page_title_of_login() == INVALID_LOGIN["title_page"]
    
    #Input login form using invalid credential and verify the result
    page.input_login_form(
        INVALID_LOGIN["username"],
        INVALID_LOGIN["password"]
    )
    assert page.get_error_message() == INVALID_LOGIN["expected_result"]