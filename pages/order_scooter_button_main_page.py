from selenium.webdriver.common.by import By
import allure
from helpers.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderScooterButton(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_order1 = (By.XPATH, "//button[@class='Button_Button__ra12g']")
        self.button_order2 = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and "
                                        "contains(@class, 'Button_Middle__1CSJM')]")
        self.open_button = (By.ID, "rcc-confirm-button")

    @allure.step('Переходим на сайт')
    def go_to_url_main(self, url):
        self.go_to_url(url)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_button(self, button_order):
        self.click_element(*self.open_button)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(button_order)
        )
        self.click_element(*button_order)
