from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path

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
        
    def double_click(self, by, locator):
        element = self.wait.until(
            EC.element_to_be_clickable((by, locator))
        )
        ActionChains(self.driver).double_click(element).perform()
        
    def right_click(self, by, locator):
        element = self.wait.until(
            EC.element_to_be_clickable((by, locator))
        )
        ActionChains(self.driver).context_click(element).perform()
    
    def click_dynamic_element(self, by, locator):
        element = self.wait.until(
            EC.element_to_be_clickable((by, locator))
        )
        ActionChains(self.driver).move_to_element(element).click().perform()
    
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
        
    def switch_to_frame(self, by, locator):
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it((by, locator))
            )

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(
            EC.visibility_of_element_located(source_locator)
        )
        target = self.wait.until(
            EC.visibility_of_element_located(target_locator)
        )

        actions = ActionChains(self.driver)
        
        actions.drag_and_drop(source, target).perform()
        
    def upload_file(self, by, locator, file_name):
        file_path = (
            Path(__file__).parent.parent
            / "data"
            / file_name
        )
        self.find(by, locator).send_keys(str(file_path))