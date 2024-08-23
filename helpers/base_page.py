from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_until(self, *locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(*locator)
        )

    def wait_for_url_change(self, current_url):
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def go_to_url(self, name_url):
        self.driver.get(name_url)

    def send_keys(self, locator, value):
        element = self.find_element(*locator)
        element.send_keys(value)

    def get_element_text(self, *locator):
        element = self.driver.find_element(*locator)
        return element.text

    def switch_to_new_window(self):
        main_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != main_window:
                self.driver.switch_to.window(window_handle)