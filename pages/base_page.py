from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(
            EC.visibility_of_element_located((by, locator))
        )

    def click(self, by, locator):
        element = self.wait.until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()
    
    def is_element_clickable(self, by, locator):
        try:
            self.wait.until(
                EC.element_to_be_clickable((by, locator))
            )
            return True

        except TimeoutException:
            return False

    def type(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def clear(self, by, locator):
        self.find(by, locator).clear()

    def get_title(self):
        return self.driver.title
    
    def get_text(self, by, locator):
        return self.find(by, locator).text
    
    def get_current_url(self):
        return self.driver.current_url
    
    def scroll_to_element(self, by, locator):
        element = self.find(by, locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )
        return element
    
    def is_element_visible(self, by, locator):
        try:
            self.wait.until(
                EC.visibility_of_element_located((by, locator))
                )
            return True
        except TimeoutException:
            return False