from selenium import webdriver
import pytest

#setup browser fixture for tests
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()