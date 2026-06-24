from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(
            EC.presence_of_element_located((by, locator))
        )

    def type(self, by, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located((by, locator))
        )
        element.clear()
        element.send_keys(text)

    def click(self, by, locator):
        element = self.wait.until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def get_title(self):
        return self.driver.title