import pytest
from pages.login_page import LoginPage
from testdata.login_data import VALID_LOGIN, INVALID_LOGIN

def test_login_success(browser):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.login(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )

    assert VALID_LOGIN["expected"] in login_page.get_expected_message()

@pytest.mark.parametrize("data", INVALID_LOGIN)
def test_login_invalid(browser, data):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.login(data["username"], data["password"])

    assert data["expected"] in login_page.get_expected_message()